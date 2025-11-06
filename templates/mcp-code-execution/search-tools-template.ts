// servers/search_tools.ts
// Progressive disclosure - search and load tools on-demand

import { readdir, readFile } from 'fs/promises';
import { join } from 'path';

/**
 * Detail level for tool discovery
 * - name: Just the tool name
 * - signature: Function signature
 * - full: Complete schema including JSDoc
 */
export type DetailLevel = 'name' | 'signature' | 'full';

/**
 * Options for searching tools
 */
export interface SearchToolsOptions {
  /** Search query (keyword or pattern) */
  query: string;

  /** How much detail to return */
  detailLevel?: DetailLevel;

  /** Filter by server name */
  server?: string;

  /** Maximum results to return */
  limit?: number;
}

/**
 * Tool definition returned by search
 */
export interface ToolDefinition {
  /** Tool name */
  name: string;

  /** Server this tool belongs to */
  server: string;

  /** File path to tool definition */
  path: string;

  /** Function signature (if detailLevel >= 'signature') */
  signature?: string;

  /** Full schema with JSDoc (if detailLevel === 'full') */
  fullSchema?: {
    description: string;
    parameters: Record<string, any>;
    returns: string;
    examples?: string[];
  };
}

/**
 * Search available MCP tools by keyword
 *
 * Enables progressive disclosure - load only the tools you need,
 * reducing token usage by up to 98.7%.
 *
 * @param options - Search options
 * @returns Array of matching tool definitions
 *
 * @example
 * ```typescript
 * // Find GitHub-related tools
 * const tools = await searchTools({
 *   query: 'github issues',
 *   detailLevel: 'signature'
 * });
 *
 * // Returns:
 * // [
 * //   {
 * //     name: 'listIssues',
 * //     server: 'github',
 * //     path: './servers/github/listIssues.ts',
 * //     signature: 'listIssues(input: ListIssuesInput): Promise<Issue[]>'
 * //   }
 * // ]
 * ```
 */
export async function searchTools(
  options: SearchToolsOptions
): Promise<ToolDefinition[]> {
  const {
    query,
    detailLevel = 'signature',
    server,
    limit = 50
  } = options;

  const results: ToolDefinition[] = [];
  const serversDir = './servers';

  try {
    // Get list of servers
    const servers = await readdir(serversDir, { withFileTypes: true });

    // Filter by server if specified
    const serversToSearch = servers
      .filter(dirent => dirent.isDirectory())
      .filter(dirent => !server || dirent.name === server)
      .filter(dirent => dirent.name !== 'utils'); // Skip utils directory

    // Search each server
    for (const serverDir of serversToSearch) {
      const serverName = serverDir.name;
      const serverPath = join(serversDir, serverName);

      // Get all .ts files in server directory
      const files = await readdir(serverPath);
      const toolFiles = files.filter(
        f => f.endsWith('.ts') && f !== 'index.ts'
      );

      // Search each tool file
      for (const file of toolFiles) {
        const toolPath = join(serverPath, file);
        const toolName = file.replace('.ts', '');

        // Read file content for searching
        const content = await readFile(toolPath, 'utf-8');

        // Check if query matches
        if (matches(content, toolName, query)) {
          const tool: ToolDefinition = {
            name: toolName,
            server: serverName,
            path: `./${join('servers', serverName, file)}`
          };

          // Add signature if requested
          if (detailLevel === 'signature' || detailLevel === 'full') {
            tool.signature = extractSignature(content, toolName);
          }

          // Add full schema if requested
          if (detailLevel === 'full') {
            tool.fullSchema = extractFullSchema(content, toolName);
          }

          results.push(tool);

          // Check limit
          if (results.length >= limit) {
            return results;
          }
        }
      }
    }

    return results;
  } catch (error) {
    console.error('Error searching tools:', error);
    return [];
  }
}

/**
 * Check if content matches search query
 */
function matches(content: string, toolName: string, query: string): boolean {
  const lowerQuery = query.toLowerCase();

  // Check tool name
  if (toolName.toLowerCase().includes(lowerQuery)) {
    return true;
  }

  // Check file content (function names, JSDoc, comments)
  if (content.toLowerCase().includes(lowerQuery)) {
    return true;
  }

  return false;
}

/**
 * Extract function signature from file content
 */
function extractSignature(content: string, toolName: string): string {
  // Find the exported function
  const regex = new RegExp(
    `export\\s+async\\s+function\\s+${toolName}\\s*\\([^)]*\\)\\s*:\\s*[^{]+`,
    'm'
  );

  const match = content.match(regex);
  if (match) {
    return match[0]
      .replace(/^export\s+async\s+function\s+/, '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  return `${toolName}(...)`;
}

/**
 * Extract full schema including JSDoc
 */
function extractFullSchema(
  content: string,
  toolName: string
): ToolDefinition['fullSchema'] {
  // Extract JSDoc comment
  const jsdocRegex = /\/\*\*[\s\S]*?\*\//g;
  const jsdocMatches = content.match(jsdocRegex) || [];

  // Find the JSDoc right before the function
  let description = '';
  let examples: string[] = [];

  for (const jsdoc of jsdocMatches) {
    // Check if this JSDoc is followed by our function
    const afterJsdoc = content.substring(
      content.indexOf(jsdoc) + jsdoc.length
    );
    if (afterJsdoc.includes(`function ${toolName}(`)) {
      // Extract description
      const descMatch = jsdoc.match(/\/\*\*\s*\n\s*\*\s*(.+)/);
      if (descMatch) {
        description = descMatch[1];
      }

      // Extract examples
      const exampleRegex = /@example[\s\S]*?```[\s\S]*?```/g;
      const exampleMatches = jsdoc.match(exampleRegex);
      if (exampleMatches) {
        examples = exampleMatches.map(ex =>
          ex.replace(/@example\s*/, '').trim()
        );
      }
      break;
    }
  }

  // Extract parameter types from interfaces
  const parameters: Record<string, any> = {};

  // Find input interface
  const inputInterfaceRegex = new RegExp(
    `export\\s+interface\\s+${capitalize(toolName)}Input\\s*{([^}]+)}`,
    's'
  );
  const inputMatch = content.match(inputInterfaceRegex);

  if (inputMatch) {
    const fields = inputMatch[1].trim().split('\n');
    for (const field of fields) {
      const fieldMatch = field.match(/(\w+)(\??):\s*([^;]+)/);
      if (fieldMatch) {
        const [, name, optional, type] = fieldMatch;
        parameters[name] = {
          type: type.trim(),
          required: !optional
        };
      }
    }
  }

  // Extract return type
  const signature = extractSignature(content, toolName);
  const returnMatch = signature.match(/:\s*Promise<(.+)>/);
  const returns = returnMatch ? returnMatch[1] : 'unknown';

  return {
    description,
    parameters,
    returns,
    ...(examples.length > 0 && { examples })
  };
}

/**
 * Capitalize first letter
 */
function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// ============================================================================
// Helper functions for using search results
// ============================================================================

/**
 * Load a tool dynamically based on search result
 *
 * @example
 * ```typescript
 * const tools = await searchTools({ query: 'github issues' });
 * const listIssues = await loadTool(tools[0]);
 * const issues = await listIssues({ repo: 'facebook/react' });
 * ```
 */
export async function loadTool(tool: ToolDefinition): Promise<any> {
  const module = await import(tool.path);
  return module[tool.name];
}

/**
 * Display search results in a readable format
 */
export function displayToolResults(tools: ToolDefinition[]): string {
  if (tools.length === 0) {
    return 'No tools found matching your query.';
  }

  let output = `Found ${tools.length} tool(s):\n\n`;

  for (const tool of tools) {
    output += `📦 ${tool.server}/${tool.name}\n`;
    output += `   Path: ${tool.path}\n`;

    if (tool.signature) {
      output += `   Signature: ${tool.signature}\n`;
    }

    if (tool.fullSchema) {
      output += `   Description: ${tool.fullSchema.description}\n`;

      if (tool.fullSchema.examples && tool.fullSchema.examples.length > 0) {
        output += `   Example: ${tool.fullSchema.examples[0]}\n`;
      }
    }

    output += '\n';
  }

  return output;
}
