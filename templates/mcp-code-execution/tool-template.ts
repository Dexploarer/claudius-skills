// servers/{server-name}/{tool-name}.ts
// Template for individual MCP tool wrappers

import { callMCPTool } from '../utils/mcp-client';

/**
 * Input interface for this tool
 * Define all parameters the tool accepts
 */
export interface ToolNameInput {
  // Add your input parameters here
  requiredParam: string;
  optionalParam?: number;
}

/**
 * Response interface for this tool
 * Define the structure of the return value
 */
export interface ToolNameResponse {
  // Add your response fields here
  id: string;
  data: any;
  metadata?: {
    timestamp: string;
    source: string;
  };
}

/**
 * [Brief description of what this tool does]
 *
 * @param input - [Description of input parameters]
 * @returns [Description of what is returned]
 *
 * @example
 * ```typescript
 * const result = await toolName({
 *   requiredParam: 'value',
 *   optionalParam: 42
 * });
 * ```
 */
export async function toolName(
  input: ToolNameInput
): Promise<ToolNameResponse> {
  // Call the underlying MCP tool
  // Replace 'mcp_tool_name' with actual MCP tool identifier
  return callMCPTool<ToolNameResponse>('mcp_tool_name', input);
}

// Example: GitHub List Issues
//
// export interface ListIssuesInput {
//   repo: string;
//   state?: 'open' | 'closed' | 'all';
//   labels?: string[];
//   assignee?: string;
// }
//
// export interface Issue {
//   number: number;
//   title: string;
//   body: string;
//   state: 'open' | 'closed';
//   labels: string[];
//   createdAt: string;
//   updatedAt: string;
// }
//
// export async function listIssues(
//   input: ListIssuesInput
// ): Promise<Issue[]> {
//   return callMCPTool<Issue[]>('github_list_issues', input);
// }
