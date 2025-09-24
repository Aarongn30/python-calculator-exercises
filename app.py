from flask import Flask, render_template, request, redirect, url_for, flash
from calc import compute

app = Flask(__name__)
app.secret_key = "dev_secret_key"

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
