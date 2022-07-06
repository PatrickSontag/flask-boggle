from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

# ? - not sure what this would be used for
debug = DebugToolbarExtension(app)
# prevents flask debugtoolbar (FDT) from stopping redirects
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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
    """Redirect to game"""

    session['guesses'] = []
    print("begin")

    return redirect ("/game")

@app.route("/game")
# @app.route("/game", methods=["POST"])
def game():
    """Show game board"""
    
    board = boggle_game.make_board()
    session["board"] = board
    print("game")

    return render_template("game.html", board=board)
    # return jsonify(board)
    # return redirect ("/", board=board)

@app.route("/check_word", methods=["POST"])
def check_word_post():
    print("check word POST")
    return "check word post"

@app.route("/check_word")
def check_word():

    print("check word")
    word = request.args["word"]
    print("word:", word)
    session['guesses'].append(word)
    print("session['guesses']:", session["guesses"])
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})
