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
    # Get the quote
    random_quote = quote_generator.generate_quote("anger")
    quote = random_quote[0]
    author = random_quote[1]
    
    # Save a random iamge
    photo_generator.get_pexels_image("1")
    
    # Edit the photo
    photo_editor = PhotoEditor(filename)
    photo_editor.edit_photo(quote, author, filename)


@app.route('/')
def index():
    # The filename the finished photo will be saved to
    filename = "static/image.JPEG"
    generate_photo(filename)    
    return render_template("index.html")