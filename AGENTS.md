# AGENTS.md

## Project Overview
This project is a minimal AI chat frontend built with:
- Python 3.12.8
- uv
- Streamlit

The application focuses on clean UX, responsive layouts, and maintainable frontend architecture.

---

## Architecture Rules
- `app.py` is the entry point only
- UI rendering belongs in `src/ui`
- API communication belongs in `src/services`
- Shared models belong in `src/models`
- Utility helpers belong in `src/utils`

Keep concerns clearly separated.

---

## Engineering Principles
Always follow:
- DRY
- KISS
- Python best practices

Prefer:
- small focused functions
- modular code
- descriptive naming
- minimal abstractions
- standard library before dependencies

Avoid overengineering.

---

## Frontend Scope
This repository is frontend-only.

Do not implement:
- LLM provider logic
- prompt orchestration
- backend business logic
- agent execution logic

Frontend communicates with backend APIs only.

---

## UI Philosophy
The interface should feel:
- minimal
- modern
- clean
- spacious
- intuitive

Inspired by modern AI chat applications like ChatGPT and Gemini.

Prioritize usability over visual complexity.