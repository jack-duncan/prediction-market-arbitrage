# Copilot Instructions

## Project Context
Building a prediction market arbitrage system that identifies and executes profitable trades between Kalshi and Polymarket. The system discovers price discrepancies on identical events across both platforms, calculates guaranteed profit opportunities, and automates bet execution to capture risk-free returns before market inefficiencies correct.

## Code Style
- Write concise, efficient Python code
- Use list/dict comprehensions over loops when clearer
- Prefer f-strings for formatting
- Use type hints for function signatures
- Keep functions under 20 lines when possible
- Do not use emojis in code or comments

## Naming Conventions
- `snake_case` for variables and functions
- `PascalCase` for classes
- `UPPER_CASE` for constants
- Descriptive names: `user_data` not `ud`

## Best Practices
- Follow DRY principle - no code duplication
- Single responsibility per function
- Handle errors explicitly with try/except
- Use context managers (`with`) for files/resources
- Add docstrings only for complex functions
- Validate inputs at function entry

## Data Processing
- Use pandas/numpy vectorized operations over loops
- Chain operations: `df.query().groupby().agg()`
- Avoid intermediate variables unless needed for clarity

## Prompt Adherence
- Follow user requirements exactly as specified
- Ask for clarification only if ambiguous
- Default to simple solutions over clever ones
- Prioritize readability and maintainability

## Avoid
- Unnecessary comments explaining obvious code
- Over-engineering simple tasks
- Nested loops when vectorization possible
- Global variables
- Magic numbers (use named constants)