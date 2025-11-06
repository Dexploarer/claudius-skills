// servers/utils/mcp-client.ts
// Wrapper for calling MCP tools from code execution environment

/**
 * Configuration for MCP client
 */
export interface MCPClientConfig {
  /** Base URL for MCP server (if using HTTP transport) */
  baseUrl?: string;

  /** Timeout for MCP calls in milliseconds */
  timeout?: number;

  /** Enable debug logging */
  debug?: boolean;
}

/**
 * MCP tool call result
 */
export interface MCPResult<T = any> {
  /** The tool's response data */
  data: T;

  /** Metadata about the call */
  metadata?: {
    duration: number;
    tokensUsed?: number;
    timestamp: string;
  };
}

/**
 * MCP client for calling tools from code execution environment
 *
 * This wrapper abstracts the underlying MCP protocol details,
 * allowing tool files to focus on business logic.
 */
class MCPClient {
  private config: MCPClientConfig;
  private static instance: MCPClient;

  private constructor(config: MCPClientConfig = {}) {
    this.config = {
      timeout: 30000,
      debug: process.env.MCP_DEBUG === 'true',
      ...config
    };
  }

  /**
   * Get singleton instance
   */
  static getInstance(config?: MCPClientConfig): MCPClient {
    if (!MCPClient.instance) {
      MCPClient.instance = new MCPClient(config);
    }
    return MCPClient.instance;
  }

  /**
   * Call an MCP tool
   *
   * @param toolName - Name of the MCP tool (e.g., 'github_list_issues')
   * @param params - Parameters to pass to the tool
   * @returns Tool response
   */
  async callTool<T = any>(
    toolName: string,
    params: Record<string, any>
  ): Promise<T> {
    const startTime = Date.now();

    try {
      if (this.config.debug) {
        console.log(`[MCP] Calling tool: ${toolName}`);
        console.log(`[MCP] Parameters:`, JSON.stringify(params, null, 2));
      }

      // This is a placeholder - actual implementation depends on your MCP setup
      // Options include:
      // 1. HTTP transport to MCP server
      // 2. Stdio transport (spawn process)
      // 3. SSE (Server-Sent Events)
      // 4. WebSocket

      const result = await this.executeToolCall(toolName, params);

      const duration = Date.now() - startTime;

      if (this.config.debug) {
        console.log(`[MCP] Tool completed in ${duration}ms`);
      }

      return result;
    } catch (error) {
      const duration = Date.now() - startTime;

      if (this.config.debug) {
        console.error(`[MCP] Tool failed after ${duration}ms:`, error);
      }

      throw new MCPError(
        `MCP tool call failed: ${toolName}`,
        'TOOL_CALL_FAILED',
        { toolName, params, error }
      );
    }
  }

  /**
   * Execute the actual MCP tool call
   * Override this method based on your transport mechanism
   */
  private async executeToolCall<T>(
    toolName: string,
    params: Record<string, any>
  ): Promise<T> {
    // IMPLEMENTATION NOTE:
    // Replace this with your actual MCP client implementation
    //
    // Example for HTTP transport:
    // const response = await fetch(`${this.config.baseUrl}/tools/${toolName}`, {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(params)
    // });
    // return response.json();
    //
    // Example for stdio transport:
    // const process = spawn('mcp-server', [toolName]);
    // process.stdin.write(JSON.stringify(params));
    // return new Promise((resolve, reject) => {
    //   process.stdout.on('data', data => resolve(JSON.parse(data)));
    //   process.stderr.on('data', reject);
    // });

    // For now, this is a placeholder that will be replaced
    // with actual MCP SDK integration
    throw new Error(
      'MCP client not configured. Implement executeToolCall() with your MCP transport.'
    );
  }

  /**
   * List available MCP tools
   */
  async listTools(): Promise<string[]> {
    // Implementation depends on MCP server capabilities
    // This would query the MCP server for available tools
    return [];
  }

  /**
   * Get tool schema
   */
  async getToolSchema(toolName: string): Promise<any> {
    // Implementation depends on MCP server capabilities
    // This would fetch the JSON schema for a specific tool
    return {};
  }
}

/**
 * Custom error for MCP operations
 */
export class MCPError extends Error {
  constructor(
    message: string,
    public code: string,
    public details?: any
  ) {
    super(message);
    this.name = 'MCPError';
  }
}

/**
 * Call an MCP tool from code execution environment
 *
 * This is the main function used by individual tool wrappers.
 *
 * @param toolName - Name of the MCP tool
 * @param params - Parameters for the tool
 * @returns Tool response
 *
 * @example
 * ```typescript
 * export async function listIssues(input: ListIssuesInput) {
 *   return callMCPTool<Issue[]>('github_list_issues', input);
 * }
 * ```
 */
export async function callMCPTool<T = any>(
  toolName: string,
  params: Record<string, any> = {}
): Promise<T> {
  const client = MCPClient.getInstance();
  return client.callTool<T>(toolName, params);
}

/**
 * Initialize MCP client with custom configuration
 *
 * Call this once at application startup if you need custom config.
 *
 * @example
 * ```typescript
 * initMCPClient({
 *   baseUrl: 'http://localhost:3000/mcp',
 *   timeout: 60000,
 *   debug: true
 * });
 * ```
 */
export function initMCPClient(config: MCPClientConfig): void {
  MCPClient.getInstance(config);
}

/**
 * List all available MCP tools
 */
export async function listMCPTools(): Promise<string[]> {
  const client = MCPClient.getInstance();
  return client.listTools();
}

/**
 * Get schema for a specific tool
 */
export async function getMCPToolSchema(toolName: string): Promise<any> {
  const client = MCPClient.getInstance();
  return client.getToolSchema(toolName);
}

// ============================================================================
// Integration Examples
// ============================================================================

/**
 * Example 1: Basic usage in a tool wrapper
 *
 * ```typescript
 * // servers/github/listIssues.ts
 * import { callMCPTool } from '../utils/mcp-client';
 *
 * export async function listIssues(input: ListIssuesInput) {
 *   return callMCPTool<Issue[]>('github_list_issues', input);
 * }
 * ```
 */

/**
 * Example 2: With error handling
 *
 * ```typescript
 * // servers/database/query.ts
 * import { callMCPTool, MCPError } from '../utils/mcp-client';
 *
 * export async function query(sql: string) {
 *   try {
 *     return await callMCPTool('database_query', { sql });
 *   } catch (error) {
 *     if (error instanceof MCPError) {
 *       console.error('Database query failed:', error.code);
 *       throw new Error(`Query failed: ${error.message}`);
 *     }
 *     throw error;
 *   }
 * }
 * ```
 */

/**
 * Example 3: Batch operations
 *
 * ```typescript
 * // servers/github/batchGetIssues.ts
 * import { callMCPTool } from '../utils/mcp-client';
 *
 * export async function batchGetIssues(numbers: number[]) {
 *   // Process in parallel in execution environment
 *   const results = await Promise.all(
 *     numbers.map(num =>
 *       callMCPTool('github_get_issue', { number: num })
 *     )
 *   );
 *
 *   // Results stay in execution environment
 *   // Only summary goes to model
 *   return {
 *     total: results.length,
 *     issues: results
 *   };
 * }
 * ```
 */
