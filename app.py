from flask import Flask, render_template, request, redirect, url_for, flash
import os
from calc import compute

app = Flask(__name__)
# Use SECRET_KEY from environment (set on Render) or fallback for local dev
app.secret_key = os.environ.get("SECRET_KEY", "dev_secret_key")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    a = request.form.get("a", "")
    b = request.form.get("b", "")
    op = request.form.get("op")
    try:
        result = compute(a, b, op)
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("index"))

    return render_template("result.html", a=a, b=b, op=op, result=result)

if __name__ == "__main__":
    app.run(debug=True)
