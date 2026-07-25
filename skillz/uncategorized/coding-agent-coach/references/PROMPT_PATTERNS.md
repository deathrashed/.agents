# Prompt Patterns for Coding Agents

Use these as templates when generating prompts. Adapt to context — do not copy placeholders literally.

---

## Debug an Error

    Debug the error: [specific error message or description]

    Goal: [what should work instead]
    Context: [relevant files, recent changes]
    Constraints: [any limits on changes]
    Process:
    - Diagnose the root cause before making any changes
    - Show your diagnosis first
    - Make the smallest fix that addresses the root cause
    - Verify the fix with: [test/build command]

---

## Add a Feature

    Add [feature name] to [file/component]

    Context: [relevant code, existing patterns]
    Requirements:
    - [specific requirement 1]
    - [specific requirement 2]
    Verification: [how to confirm it works]
    Process:
    - Show your implementation plan first
    - Make small, incremental changes
    - Confirm before large refactors
    - Run [test/build command] when done

---

## Refactor Safely

    Refactor [what] to follow [pattern/goal]

    Why: [benefit]
    Constraints:
    - Do not change external behavior
    - Keep existing tests passing
    - [other limits]
    Process:
    1. Identify all places that need to change
    2. Make changes incrementally
    3. Run [test suite] after each change
    4. Report what changed and confirm tests still pass

---

## Write Tests

    Add tests for [function/component]

    Test framework: [e.g. Jest, pytest, go test]
    Required coverage:
    - [case 1]
    - [case 2]
    - Edge cases: [list]
    Context: [where the code lives, fixtures needed]
    Process:
    - Do not change production code unless a bug is found
    - Run the test suite and confirm all tests pass
    - Report coverage or list what was added

---

## Investigate / Explore

    Investigate [topic/area]

    Goal: [what to understand]
    Already known: [what was already tried or found]
    Focus on:
    - Finding the relevant code or patterns
    - Explaining how it works
    - Identifying risks or gaps
    - Suggesting concrete next steps
    Do not make any changes yet.

---

## Stuck / Reset

    Stop. Do not make any more edits.

    Goal: [clear, specific goal restated]
    Current state: [files, errors, what has been tried]
    Process:
    - Inspect the relevant files and summarize what you find
    - Identify the single root cause of the failure
    - Propose a plan with steps before making any changes
    - Wait for confirmation before proceeding
    - Make one change at a time and verify after each

---

## Code Review Request

    Review [file/component] for [specific concern]

    Focus on:
    - [concern 1]
    - [concern 2]
    Criteria:
    - Does it meet the requirements?
    - Are there bugs or edge cases not handled?
    - Any fragile patterns, code smells, or risks?
    Do not make changes — report findings only.

---

## Extract / Modularize

    Extract [what] from [current file] into [target file/module]

    Requirements:
    - Keep existing behavior identical
    - Update all callers
    - Add tests for the new module
    Process:
    - Show the plan and new module interface first
    - Confirm before making changes
    - Run [test suite] after and confirm all tests pass
