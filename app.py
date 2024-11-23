from edit_photos import photo_editor
from generate_photos import photo_generator
from generate_quotes import quote_generator

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")