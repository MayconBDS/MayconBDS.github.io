import os
from flask import Flask, render_template

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    print("Página inicial acessada")
    return render_template("index.html")

@app.route("/moments")
def moments():
    return render_template("moments.html")

if __name__ == "__main__":
    print("Rodando o app Flask...")
    app.run(debug=True)
