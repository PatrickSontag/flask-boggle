from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

boggle_game = Boggle()

@app.route("/")
def home():
    return render_template("home.html")