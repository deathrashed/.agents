# Prompt Patterns for Coding Agents

Use these patterns when generating prompts in Step 4. Adjust placeholders to context.

## Debug an Error

```
Debug the error: [specific error message or description]

Goal: [what should work instead]
Context: [relevant files, recent changes]
Constraints: [any limits on changes]
Requirements:
- Diagnose the root cause first
- Show your diagnosis before making changes
- Verify the fix works
```

## Add a Feature

```
Add [feature name] to [file/component]

Requirements:
- [specific requirement 1]
- [specific requirement 2]
Context: [relevant code, existing patterns]
Test: [how to verify it works]
Requirements:
- Show your implementation plan first
- Make small, incremental changes
- Confirm before large refactors
```

## Refactor Safely

```
Refactor [what to refactor] to follow [pattern/name]

Why: [benefit of refactor]
Constraints:
- Don't change external behavior
- Keep existing tests passing
- [other limits]
Steps:
1. Identify all places needing change
2. Make changes incrementally
3. Run [test suite] after each change
```

## Write Tests

```
Add tests for [function/component]

Test framework: [e.g., Jest, pytest]
Coverage requirements:
- [specific case 1]
- [specific case 2]
- Edge cases: [list]
Context: [where the code lives, any fixtures needed]
```

## Investigate / Explore

```
Investigate [topic/area]

Goal: [what to understand]
Already known: [what user already tried]
Focus on:
- Finding the relevant code/patterns
- Explaining how it works
- Suggesting next steps
```

## Stuck / Reset

```
Start fresh. Goal: [clear, specific goal]

What exists: [files, current state]
Approach:
- Build incrementally
- Show plan first before implementing
- Test after each step
- Confirm before proceeding to next
```

## Code Review Request

```
Review [file/component] for [issue]

Focus on:
- [specific concern 1]
- [specific concern 2]
Criteria:
- Does it meet the requirements?
- Are there any bugs?
- Any code smells or risks?
```

## Extract / Modularize

```
Extract [what] into [new module/component]

Current location: [file]
Target location: [where]
Requirements:
- Keep existing behavior
- Update all callers
- Add tests for the new module
```