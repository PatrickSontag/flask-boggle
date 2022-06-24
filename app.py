from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

boggle_game = Boggle()

@app.route("/")
def home():

    board = boggle_game.make_board()
    # session['board'] = board
    # print(session['board'])
    print("board: ", board)
    print("session: ", session)

    return render_template("home.html", board=board)