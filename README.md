# GTA Greal Deals AI Agent (Frontend)

## Background

This repository serves the frontend UI of the AI agent project.

## Set up

### Python Version

Python 3.12.8 is used in this project.

### Python Package Manager

uv is used for the package manager given its robustness and performance.

Make sure you have uv installed in your environment.

```bash
pip install uv
```

### Python Virtual Environement

It is always a best practice to create a virtual environment for running a Python project instead of the global python environment.

Make sure you create and activate the project virtual environment.

```bash
uv venv ./venv
source ./venv/Scripts/activate
```

### Project Dependency

Install required dependencies

```bash
uv pip install -r requirements.txt
```

### Run Application

Simply run the `.run.sh` shell script in your terminal to host the application.

```bash
./run.sh
```

You should be able to access the application locally on specific port.