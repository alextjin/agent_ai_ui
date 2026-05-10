# AI Chat Frontend

## Overview

Minimal Streamlit frontend for an AI chat interface. The app is frontend-only:
it manages chat UI state, renders messages, and previews streaming assistant
responses without implementing provider or backend logic.

## Structure

- `app.py` - entry point only
- `src/ui` - Streamlit rendering components
- `src/models` - shared data models
- `src/utils` - session state helpers

## Setup

Python 3.12.8 is used in this project.

Install `uv` if needed:

```bash
pip install uv
```

Create and activate the virtual environment:

```bash
uv venv ./venv
source ./venv/Scripts/activate
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

Run the app:

```bash
./run.sh
```

The app will be available on the local Streamlit URL shown in the terminal.
