from edit_photos import PhotoEditor
from generate_photos import photo_generator
from generate_quotes import quote_generator

from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    filename = "static/image.JPEG"
    quote = quote_generator.generate_quote("anger")
    photo = photo_generator.get_pexels_image("1")
    img = Image.open(filename)
    photo_editor = PhotoEditor(img)
    photo_editor.edit_photo(quote[0], quote[1], filename)
    return render_template("index.html")