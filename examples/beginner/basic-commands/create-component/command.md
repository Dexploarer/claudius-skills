Create a new component file with basic boilerplate.

Arguments: $ARGUMENTS (component name and optionally type/framework)

Process:
1. Parse the component name from $ARGUMENTS
2. Detect framework from project files (package.json, requirements.txt, etc.)
3. Create appropriate boilerplate:

   **For React/TypeScript projects:**
   - Create `ComponentName.tsx`
   - Include React import
   - Export component with TypeScript props interface
   - Add basic styling setup

   **For Vue projects:**
   - Create `ComponentName.vue`
   - Include template, script, and style sections
   - Use Composition API if detected

   **For Python/Django:**
   - Create appropriate view or model file
   - Include Django imports

4. Ask if user wants a test file created too
5. Display next steps (import it, add props, etc.)

Example usage:
- `/create-component Button`
- `/create-component UserCard react`
- `/create-component TodoList vue`
