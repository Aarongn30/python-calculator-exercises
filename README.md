# Simple Flask Calculator

A tiny beginner-friendly Flask web app that performs basic arithmetic (add, subtract, multiply, divide).

Getting started (Windows PowerShell):

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run locally (development server):

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Deployment suggestions:
- Render.com or Replit: connect the repository and use the `web: gunicorn app:app` command as the start command.
- Heroku (deprecated by many but still possible): use the included `Procfile`.

Notes for beginners:
- The calculation logic lives in `calc.py` and is easy to test.
- Try editing the UI in `templates/index.html` and reloading the page.

Tests:

Run:

```powershell
pytest -q
```
