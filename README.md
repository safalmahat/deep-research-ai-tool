## Deep Research AI Tool

A project for an agentic AI "deep research" tool.

### Features (scaffold)
- **CLI entrypoint**: `python main.py`
- **API integrations**: `openai`, `requests`
- **UI-ready**: `gradio` available for a quick web UI
- **Document ingestion**: `pypdf` for PDF parsing
- **Environment management**: `python-dotenv` for `.env`

## Requirements
- **Python**: 3.12+
- **OS**: Windows, macOS, or Linux
- **OpenAI API key** (optional for now, required once you integrate OpenAI): create a free key and store it in `.env` as `OPENAI_API_KEY`.

## Quickstart

### 1) Clone the repo
```bash
git clone https://github.com/safalmahat/deep-research-ai-tool.git deep-research-ai-tool
cd deep-research-ai-tool
```

### 2) Create and activate a virtual environment (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure environment variables
Create a `.env` file in the project root (same folder as `main.py`):
```bash
echo OPENAI_API_KEY=sk-your-key-here > .env
```

Alternatively, create the file manually with this content:
```
OPENAI_API_KEY=sk-your-key-here
```

### 5) Run the app
```bash
python main.py
```

You should see:
```

```

## Project Structure
```
deep-research-ai-tool/
├─ main.py               # CLI entrypoint (current demo prints a greeting)
├─ requirements.txt      # Runtime dependencies
├─ pyproject.toml        # Project metadata (name, version, Python requirement)
└─ README.md             # This file
```

## Configuration & Secrets
- **`.env`**: Loaded via `python-dotenv`. Typical variables:
  - `OPENAI_API_KEY`: required once you use the OpenAI API.
- Never commit real secrets to Git. Prefer environment variables or a secrets manager.

## Development Notes
- Code style: prefer descriptive variable names and clear control flow.
- Python 3.12 is specified in `pyproject.toml`. If you use a different version, update that file accordingly.
- If you add a Gradio UI, create a separate module (for example, `app/ui.py`) and keep `main.py` small (just CLI/bootstrap).

## Extending the Tool (next steps)
Here are suggested enhancements you can implement incrementally:
- Hook up the OpenAI client and add a simple research prompt flow.
- Build a `gradio` interface for inputs (query, sources) and outputs (findings, citations).
- Add PDF ingestion with `pypdf` and chunking + embeddings for retrieval.
- Create a config module (for example, `app/config.py`) to centralize `.env` handling and defaults.
- Add tests and CI (for example, `pytest`, GitHub Actions).

## Troubleshooting
- If the command is not found on Windows when activating venv, ensure PowerShell execution policy allows scripts: run PowerShell as Administrator and execute:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- If `openai` calls fail, ensure `OPENAI_API_KEY` is set and your account has access.
- If dependency issues arise, try upgrading `pip` and reinstalling:
  ```bash
  python -m pip install --upgrade pip
  pip install -r requirements.txt --upgrade
  ```

## License



