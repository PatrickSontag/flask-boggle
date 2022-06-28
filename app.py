from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session, redirect, flash
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

boggle_game = Boggle()

@app.route("/")
def home():
    """Generate and show form to start game"""

    # print("board: ", board)
    # print("session: ", session)
    print("home")

    return render_template("home.html")

@app.route("/begin", methods=["POST"])
def begin():
    """Redirect to new game"""

    session['guesses'] = []
    print("begin")

    return redirect ("/new_game")

@app.route("/new_game")
def new_game():
    """Show new game board"""
    
    board = boggle_game.make_board()
    session['board'] = board
    print("new game")

    return render_template("new_game.html", board=board)