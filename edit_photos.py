from PIL import Image, ImageDraw
from random import randint

from globals import FILENAME, SAVE_AS
from text import Text

class PhotoEditor:
    def __init__(self):
        """
        Initialize a PhotoEditor object.

        Args:
            None

        Attributes:
            save_as (str): The filename to save the edited image as.
            photo (Image): The image to be edited.
            width (int): The width of the image.
            height (int): The height of the image.
            draw (ImageDraw.Draw): The drawing context used to edit the image.
            rectangle_x0 (int): The x-coordinate of the top-left corner of the rectangle to be drawn over the image.
            rectangle_x1 (int): The x-coordinate of the bottom-right corner of the rectangle to be drawn over the image.
            rectangle_y0 (int): The y-coordinate of the top-left corner of the rectangle to be drawn over the image.
            rectangle_y1 (int): The y-coordinate of the bottom-right corner of the rectangle to be drawn over the image.

        Returns:
            None
        """
        self.photo = Image.open(FILENAME)
        self.width, self.height = self.photo.size
        self.draw = ImageDraw.Draw(self.photo, "RGBA")
        
        # This is the offset of the rectangle that is drawn over the photo for better readability
        RECTANGLE_X_OFFSET = 50
        RECTANGLE_Y_OFFSET = 100 
        
        # This is the rectangle 's xy coordinates
        self.rectangle_x0 = RECTANGLE_X_OFFSET
        self.rectangle_x1 = self.width - RECTANGLE_X_OFFSET
        self.rectangle_y0 = RECTANGLE_Y_OFFSET
        self.rectangle_y1 = self.height - RECTANGLE_Y_OFFSET
        
    
    def draw_rectangle(self):
        """
        Draw a semi-transparent rectangle on the photo, starting at the top-left corner defined by (x0, y0) and ending at the bottom-right corner defined by (x1, y1). This allows for better readability of the text on the background. The fill color is white with some transparency, and the outline is a solid white line.
        
        Returns:
            None
        """
        
        xy = (self.rectangle_x0, self.rectangle_y0, self.rectangle_x1, self.rectangle_y1)
        transparency = randint(100, 230)
        self.draw.rectangle(
            xy = xy, 
            fill = (255, 255, 255, transparency), 
            outline = (255, 255, 255), 
        )
        
    def draw_author(self, author):
        """
        Draw the author of the quote on the photo.
        
        The author is drawn centered horizontally and vertically on the rectangle drawn in 'draw_rectangle()', and is below the quote.
        
        Args:
            author (str): The author of the quote.
        
        Returns:
            None
        """
        RECTANGLE_WIDTH = self.rectangle_x1 - self.rectangle_x0
        RECTANGLE_HEIGHT = self.rectangle_y1 - self.rectangle_y0
        
        VERTICAL_PADDING = 50
        HORIZONTAL_PADDING = 50
        
        # Add a '-' to the beginning of the author to signify that they said the quote
        author = "- " + author
        
        author_font_size = randint(170, 250)
        author_text = Text(author, font_path="fonts/georgiai.ttf", font_size=author_font_size)
        
        # Get the wrapped text of the author
        wrapped_author_text = author_text.wrap_text(RECTANGLE_WIDTH)
        
        author_fill = (0, 0, 0)
        # Draw the author
        for i, line in enumerate(wrapped_author_text):
            line_xy = line.get_center_coordinates(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
            
            # Add padding between the left edge of the rectangle and text
            actual_x = line_xy[0] + HORIZONTAL_PADDING
            
            # Set the y value of the line to the bottom of the quote
            actual_y = line_xy[1] + self.quote_text.height * (3 - i) + 200
            
            # Add padding between each line of text
            actual_y -= VERTICAL_PADDING
            
            line_xy = [actual_x, actual_y]
            line.draw(self.draw, line_xy, author_fill)
        
        
    def draw_quote(self, quote):
        """
        Draw the quote on top of the photo. It is centered horizontally and vertically on the rectangle drawn in 'draw_rectangle()'.
        
        Args:
            quote (str): The quote to be drawn on the photo.
            author (str): The author of the quote, which is drawn directly below the quote.

        Returns:
            None
        """
        RECTANGLE_WIDTH = self.rectangle_x1 - self.rectangle_x0
        RECTANGLE_HEIGHT = self.rectangle_y1 - self.rectangle_y0
        
        quote_font_size = randint(250, 300)
        
        # Since this object is accessed in 'draw_author()', it is set as an object variable.
        self.quote_text = Text(quote, font_path="fonts/georgia.ttf", font_size=quote_font_size)
        
        VERTICAL_PADDING = 50
        HORIZONTAL_PADDING = 50
        
        quote_fill = (0, 0, 0)
        
        # Get the wrapped text
        wrapped_quote_text = self.quote_text.wrap_text(RECTANGLE_WIDTH)
        
        # Draw the quote
        for i, line in enumerate(wrapped_quote_text):
            # Used to adjust the vertical offset of each line based on the line's position in the list
            line_offset = len(wrapped_quote_text) // 3
            
            line_xy = line.get_center_coordinates(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
            
            # Add padding between the left edge of the rectangle and text
            actual_x = line_xy[0] + HORIZONTAL_PADDING
            
            # Adjust the y value of the line based on its position in the list
            actual_y = line_xy[1] - line.height * (i - line_offset)
            
            # Add padding between each line of text
            actual_y -= VERTICAL_PADDING * i
            
            line_xy = [actual_x, actual_y]
            line.draw(self.draw, line_xy, quote_fill)
    
    
    def save_photo(self):
        """
        Save the edited photo to the path specified in 'SAVE_AS'.
        
        Returns:
            None
        """
        self.photo.save(SAVE_AS)
    
    
    def edit_photo(self, quote, author):
        """
        Execute both 'draw_rectangle()' and 'draw_quote()', and save the Image to 'file'.
        
        Args:
            quote (str): The quote to be drawn on the photo.
            author (str): The author of the quote, which is drawn directly below the quote.

        Returns:
            None
        """
        self.draw_rectangle()
        self.draw_quote(quote)
        self.draw_author(author)
        self.save_photo()