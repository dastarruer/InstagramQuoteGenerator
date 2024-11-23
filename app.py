from edit_photos import PhotoEditor
from generate_photos import photo_generator
from generate_quotes import quote_generator

from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)


def generate_photo(filename):
    """
    Generate a photo by overlaying a quote onto an image sourced from Pexels, then save the edited image to 'filename'.
    """
    random_quote = quote_generator.generate_quote("anger")
    quote = random_quote[0]
    author = random_quote[1]
    photo_generator.get_pexels_image("1")
    
    img = Image.open(filename)
    photo_editor = PhotoEditor(img)
    photo_editor.edit_photo(quote, author, filename)


@app.route('/')
def index():
    filename = "static/image.JPEG"
    create_photo(filename)    
    return render_template("index.html")