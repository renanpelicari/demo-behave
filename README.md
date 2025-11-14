# Behame Framework Demo

A simple demonstration of **Behavior-Driven Development (BDD)** in Python using the [Behave](https://behave.readthedocs.io/) framework.

- **Tests**: Located in `/tests/behave`
- **Application**: Located in `/src` (a FastAPI app for managing movies and books)

> **Note:** This API is for demo purposes only. It does **not** use persistent storage. Restarting the app will reset all data.

---

## ✅ Environment Setup

### Prerequisites
- Python **3.12+**

[//]: # (- [Docker]&#40;https://www.docker.com/&#41; *&#40;optional&#41;*)
- Virtual environment *(recommended)*

### Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```
Or specify Python version:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install poetry
poetry install
```

---

## ▶️ Run the Application

Start the app before running tests.

[//]: # (#### Using Docker)

[//]: # (```bash)

[//]: # (docker build -t demo-behave-api .)

[//]: # (docker run -d -p 8000:8000 demo-behave-api)

[//]: # (```)

#### Using Poetry
```bash
poetry run python src/main.py
```

---

## 🧪 Run Tests

From the project root, run:

```bash
behave
```

You can select specific features, scenarios, or tags.
Chose to show the output in different formats (e.g., `--format pretty`, `--format json`).

And many other options, here is an example:

```bash
behave --tags=@movies --format pretty
```

However you do not need to specify this manually every time, you can edit the file [behave.ini](behave.ini) to set your preferred options.

This file contains the default configuration for Behave.

---

## ✍️ Create Test Scenarios

A Behave project includes:
- **Feature files**: Written in Gherkin syntax
- **Step definitions**: Python functions implementing steps
- **Environment config**: Setup/teardown logic
- **Hooks**: Modify test execution behavior
- **Config files**: Behave settings
- **Reports**: Test results summary
- **Utilities & Data files**: Helpers and test data

### Steps to Create:
1. **Define Feature**: Add `.feature` file in `features/`
2. **Write Steps**: Add Python step definitions in `features/steps/`

Use the existing `movies.feature` as a reference.
