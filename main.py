from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Página inicial"

@app.route("/moments")
def moments():
    return render_template("moments.html")

app.run(host='0.0.0.0', port=81)