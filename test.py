from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "kjsdf"

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

