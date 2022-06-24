from boggle import Boggle
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

boggle_game = Boggle()
