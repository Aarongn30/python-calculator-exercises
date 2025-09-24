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

Deploying to Render
-------------------

1. Push your repo to GitHub (already done).
2. Go to https://render.com and create an account or sign in.
3. Click "New" → "Web Service" → "Connect a repository" and select this repository.
4. Set the branch to `main`.
5. For the Start Command use:

```
gunicorn app:app
```

Render will install dependencies from `requirements.txt` and deploy the app. The included `render.yaml` enables automatic deploy configuration if you use Render's git-based setup.
