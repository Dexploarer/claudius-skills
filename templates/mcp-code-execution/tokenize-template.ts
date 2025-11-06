// servers/utils/tokenize.ts
// PII tokenization for privacy-preserving MCP operations

/**
 * Token map storing original values
 * In production, consider using encrypted storage
 */
const tokenMap = new Map<string, string>();
const reverseTokenMap = new Map<string, string>();

/**
 * Tokenization statistics
 */
export interface TokenizationStats {
  emailsTokenized: number;
  phonesTokenized: number;
  ssnTokenized: number;
  customTokenized: number;
  totalTokens: number;
}

const stats: TokenizationStats = {
  emailsTokenized: 0,
  phonesTokenized: 0,
  ssnTokenized: 0,
  customTokenized: 0,
  totalTokens: 0
};

/**
 * Patterns for common PII
 */
const PII_PATTERNS = {
  email: /[\w.-]+@[\w.-]+\.\w+/g,
  phone: /\b(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/g,
  ssn: /\b\d{3}-\d{2}-\d{4}\b/g,
  creditCard: /\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b/g,
  ipAddress: /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/g
};

/**
 * Custom tokenization pattern
 */
export interface CustomPattern {
  name: string;
  pattern: RegExp;
  prefix: string;
}

const customPatterns: CustomPattern[] = [];

/**
 * Tokenize PII in text
 *
 * Replaces sensitive information with tokens like [EMAIL_1], [PHONE_1], etc.
 * The original values are stored securely and can be retrieved later.
 *
 * **Use case:** Prevent model from seeing PII while still allowing
 * MCP tools to access real values via untokenize().
 *
 * @param text - Text containing potential PII
 * @param options - Tokenization options
 * @returns Text with PII replaced by tokens
 *
 * @example
 * ```typescript
 * const data = "Contact john@example.com at 555-123-4567";
 * const safe = tokenizePII(data);
 * // Returns: "Contact [EMAIL_1] at [PHONE_1]"
 *
 * // Model sees safe version
 * const analysis = await analyzeText(safe);
 *
 * // When sending email, untokenize
 * await sendEmail({
 *   to: untokenize('[EMAIL_1]'),  // Real email
 *   subject: 'Follow up'
 * });
 * ```
 */
export function tokenizePII(
  text: string,
  options: {
    /** Tokenize emails (default: true) */
    emails?: boolean;
    /** Tokenize phone numbers (default: true) */
    phones?: boolean;
    /** Tokenize SSNs (default: true) */
    ssn?: boolean;
    /** Tokenize credit cards (default: true) */
    creditCards?: boolean;
    /** Tokenize IP addresses (default: false) */
    ipAddresses?: boolean;
    /** Tokenize custom patterns */
    custom?: boolean;
  } = {}
): string {
  const {
    emails = true,
    phones = true,
    ssn = true,
    creditCards = true,
    ipAddresses = false,
    custom = true
  } = options;

  let result = text;

  // Tokenize emails
  if (emails) {
    result = result.replace(PII_PATTERNS.email, (match) => {
      const token = createToken('EMAIL', match);
      stats.emailsTokenized++;
      return token;
    });
  }

  // Tokenize phone numbers
  if (phones) {
    result = result.replace(PII_PATTERNS.phone, (match) => {
      const token = createToken('PHONE', match);
      stats.phonesTokenized++;
      return token;
    });
  }

  // Tokenize SSNs
  if (ssn) {
    result = result.replace(PII_PATTERNS.ssn, (match) => {
      const token = createToken('SSN', match);
      stats.ssnTokenized++;
      return token;
    });
  }

  // Tokenize credit cards
  if (creditCards) {
    result = result.replace(PII_PATTERNS.creditCard, (match) => {
      const token = createToken('CC', match);
      stats.customTokenized++;
      return token;
    });
  }

  // Tokenize IP addresses
  if (ipAddresses) {
    result = result.replace(PII_PATTERNS.ipAddress, (match) => {
      // Skip common non-IP patterns like version numbers
      if (match.startsWith('0.') || match.startsWith('1.0')) {
        return match;
      }
      const token = createToken('IP', match);
      stats.customTokenized++;
      return token;
    });
  }

  // Tokenize custom patterns
  if (custom) {
    for (const pattern of customPatterns) {
      result = result.replace(pattern.pattern, (match) => {
        const token = createToken(pattern.prefix, match);
        stats.customTokenized++;
        return token;
      });
    }
  }

  return result;
}

/**
 * Create a token and store the mapping
 */
function createToken(prefix: string, value: string): string {
  // Check if we already have a token for this value
  const existing = reverseTokenMap.get(value);
  if (existing) {
    return existing;
  }

  // Create new token
  const count = Array.from(tokenMap.keys()).filter(k =>
    k.startsWith(`[${prefix}_`)
  ).length + 1;

  const token = `[${prefix}_${count}]`;

  // Store both directions
  tokenMap.set(token, value);
  reverseTokenMap.set(value, token);
  stats.totalTokens++;

  return token;
}

/**
 * Untokenize a token back to its original value
 *
 * Use this when passing data to MCP tools that need real values.
 *
 * @param token - Token to untokenize (e.g., '[EMAIL_1]')
 * @returns Original value, or token if not found
 *
 * @example
 * ```typescript
 * const email = untokenize('[EMAIL_1]');
 * await sendEmail({ to: email, subject: 'Hi' });
 * ```
 */
export function untokenize(token: string): string {
  return tokenMap.get(token) || token;
}

/**
 * Untokenize all tokens in text
 *
 * @param text - Text containing tokens
 * @returns Text with all tokens replaced by original values
 *
 * @example
 * ```typescript
 * const safe = "Contact [EMAIL_1] at [PHONE_1]";
 * const real = untokenizeAll(safe);
 * // Returns: "Contact john@example.com at 555-123-4567"
 * ```
 */
export function untokenizeAll(text: string): string {
  let result = text;

  for (const [token, value] of tokenMap.entries()) {
    result = result.replace(new RegExp(escapeRegex(token), 'g'), value);
  }

  return result;
}

/**
 * Escape special regex characters
 */
function escapeRegex(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/**
 * Register a custom tokenization pattern
 *
 * @example
 * ```typescript
 * // Tokenize API keys
 * addCustomPattern({
 *   name: 'api-keys',
 *   pattern: /sk-[a-zA-Z0-9]{32}/g,
 *   prefix: 'API_KEY'
 * });
 *
 * const text = "Use key sk-abc123xyz456...";
 * const safe = tokenizePII(text, { custom: true });
 * // Returns: "Use key [API_KEY_1]"
 * ```
 */
export function addCustomPattern(pattern: CustomPattern): void {
  customPatterns.push(pattern);
}

/**
 * Remove a custom pattern
 */
export function removeCustomPattern(name: string): void {
  const index = customPatterns.findIndex(p => p.name === name);
  if (index !== -1) {
    customPatterns.splice(index, 1);
  }
}

/**
 * Clear all tokens (for testing or session reset)
 */
export function clearTokens(): void {
  tokenMap.clear();
  reverseTokenMap.clear();
  stats.emailsTokenized = 0;
  stats.phonesTokenized = 0;
  stats.ssnTokenized = 0;
  stats.customTokenized = 0;
  stats.totalTokens = 0;
}

/**
 * Get tokenization statistics
 */
export function getTokenizationStats(): TokenizationStats {
  return { ...stats };
}

/**
 * Check if text contains any tokens
 */
export function hasTokens(text: string): boolean {
  return /\[(?:EMAIL|PHONE|SSN|CC|IP|[A-Z_]+)_\d+\]/.test(text);
}

/**
 * Extract all tokens from text
 */
export function extractTokens(text: string): string[] {
  const matches = text.match(/\[(?:EMAIL|PHONE|SSN|CC|IP|[A-Z_]+)_\d+\]/g);
  return matches || [];
}

/**
 * Get all tokenized values (for debugging/auditing)
 *
 * WARNING: This exposes PII! Only use for debugging in secure environments.
 */
export function getAllTokenMappings(): Map<string, string> {
  return new Map(tokenMap);
}

// ============================================================================
// Integration Examples
// ============================================================================

/**
 * Example 1: Safe data processing
 *
 * ```typescript
 * import { tokenizePII, untokenize } from './servers/utils/tokenize';
 *
 * // Load sensitive data
 * const userData = await getUserData();
 *
 * // Tokenize before model sees it
 * const safeData = tokenizePII(userData.profile);
 *
 * // Model processes tokenized version
 * const analysis = await analyzeProfile(safeData);
 * // Model sees: "Contact [EMAIL_1] at [PHONE_1]"
 *
 * // When sending notification, untokenize
 * await sendEmail({
 *   to: untokenize('[EMAIL_1]'),  // Real email
 *   subject: 'Your analysis is ready'
 * });
 * ```
 */

/**
 * Example 2: Batch processing with PII
 *
 * ```typescript
 * // Process 1000 customer records
 * const customers = await loadCustomers();
 *
 * // Tokenize all PII
 * const safeCustomers = customers.map(c => ({
 *   ...c,
 *   email: tokenizePII(c.email),
 *   phone: tokenizePII(c.phone)
 * }));
 *
 * // Model analyzes tokenized data (no PII exposure)
 * const insights = await analyzeCustomers(safeCustomers);
 *
 * // Send results to real customers
 * for (const customer of customers) {
 *   await sendReport({
 *     to: customer.email,  // Real email
 *     data: insights[customer.id]
 *   });
 * }
 * ```
 */

/**
 * Example 3: Logging without PII
 *
 * ```typescript
 * function safeLog(message: string) {
 *   // Automatically tokenize before logging
 *   const safe = tokenizePII(message);
 *   console.log(safe);
 *   // Logs: "User [EMAIL_1] logged in from [IP_1]"
 *   // Instead of: "User john@example.com logged in from 192.168.1.1"
 * }
 * ```
 */
