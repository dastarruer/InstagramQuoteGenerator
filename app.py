from edit_photos import PhotoEditor
from generate_photos import photo_generator
from generate_quotes import quote_generator

from flask import Flask, render_template, request


FILENAME = "static/images/image.JPEG"
SAVE_AS = "static/images/edited_image.JPEG"

app = Flask(__name__)


def generate_custom_photo_quote(quote, author, filename, save_as):
    # Save a random iamge from the Pexels API
    photo_generator.save_pexels_image(1)
    
    # Edit the photo and save it
    photo_editor = PhotoEditor(filename, save_as)
    photo_editor.edit_photo(quote, author)


def generate_random_photo_quote(filename, save_as):
    """
    Generate a photo by overlaying a random quote from the API Ninjas Quote API onto an image sourced from the Pexels API, then save the edited image to 'filename'.
    """
    # Get the quote
    random_quote = quote_generator.generate_quote("anger")
    quote = random_quote[0]
    author = random_quote[1]
    
    # Save a random iamge from the Pexels API
    photo_generator.save_pexels_image(1)
    
    # Edit the photo and save it
    photo_editor = PhotoEditor(filename, save_as)
    photo_editor.edit_photo(quote, author)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        author = request.form['author']
        
        # If the user does not input anything, put the error message in the photo (genius I know)
        if not quote:
            quote = "Hey! you forgot the quote"
        if not author:
            author = "You, my friend."
        generate_custom_photo_quote(quote, author, FILENAME, SAVE_AS)
        return render_template("index.html", quote=quote)
    generate_random_photo_quote(FILENAME, SAVE_AS)    
    return render_template("index.html", quote=quote)