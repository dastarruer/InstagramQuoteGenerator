from PIL import Image, ImageFont, ImageDraw


class Text:
    def __init__(self, text: str, font: ImageFont = None, font_path: str = None, font_size: int = None):
        """
        Initialize a Text object.

        Args:
            text (str): The text to be displayed.
            font (ImageFont): The font of the text. If not specified, a font will be created using font_path and font_size.
            font_path (str): The path to the font file. Only used if font is not specified.
            font_size (int): The size of the font. Only used if font is not specified.

        Returns:
            None
        """
        self.text = text
        self.font = font
        # If a font is not specified, use font_path and font_size as optional arguments to create the font
        if not self.font:
            self.font = ImageFont.truetype(font_path, font_size)
    
    
    @property
    def width(self):
        """
        The width of the rendered text.

        The width is calculated as the absolute difference between the x-coordinates of the
        top-left and bottom-right corners of the text's bounding box.

        Returns:
            int: The width of the rendered text.
        """
        bbox = self.font.getbbox(self.text)
        width = abs(bbox[0] - bbox[2])
        return width
    
    
    @property
    def height(self):
        """
        The height of the rendered text.

        The height is calculated as the absolute difference between the y-coordinates of the
        top-left and bottom-right corners of the text's bounding box.

        Returns:
            int: The height of the rendered text.
        """
        bbox = self.font.getbbox(self.text)
        height = abs(bbox[1] - bbox[3])
        return height
    
    def wrap_text(self, max_width: int):
        """
        Wrap the text to fit within the specified maximum width.

        This method breaks the input text into multiple lines, ensuring that each line's width 
        does not exceed the given `max_width`. Words are added to the current line until adding
        another word would exceed the width limit, at which point the word is moved to a new line.

        Args:
            max_width (int): The maximum width (in pixels) that a single line of text can occupy.

        Returns:
            list[Text]: A list of `Text` objects representing the wrapped lines of text. Each `Text` object contains a portion of the original text, and the list is reversed to display the 
                first lines at the top.
        """
        lines = []
        words = self.text.split(" ")
        
        # Stores the current line, and is appended to 'lines' once its width exceeds 'max_width'.
        current_line = Text("", font=self.font)
        
        for word in words:
            # Store the current word as a Text object, adding a trailing space
            # Without the trailing space, the line 'Who am I?' would instead become 'WhoamI?'
            word = Text(word + " ", font=self.font)
            if word.width + current_line.width >= max_width:
                # If 'line' was set to 'current_line', any changes made to 'current_line' would also be applied to 'line'. 
                # So, we have to make an entirely new object.
                line = Text(current_line.text, font=self.font)
                lines.append(line)
                
                # Set 'current_line' to 'word.text' instead of an empty string to ensure current word is included
                current_line.text = word.text
            else:
                current_line.text += word.text
        # Append current_line, so that the last line does not get left out
        lines.append(current_line)
        
        # Reverse list to show the first lines at the top, and the last lines at the bottom
        return lines[::-1]
    
        
    def get_center_coordinates(self, bbox_width, bbox_height):
        """
        Get the coordinates that would center the text in a given bounding box.
        
        This method takes `bbox_width` and `bbox_height`, and subtracts the width and height of the text respectively. This is then divided by 2, and floored, which returns the coordinates that would center the text inside of the bounding box.
        
        Args:
            bbox_width (int): The width of the bounding box that the text is to be centered in.
            bbox_height (int): The height of the bounding box that the text is to be centered in.

        Returns:
            center[center_x (int), center_y] (int): The coordinates that the text should be drawn at in order to center it inside of the bounding box. 
        """
        center_x = (bbox_width - self.width) // 2
        center_y = (bbox_height - self.height) // 2
        
        # This is not a tuple, because these values usually need to be changed later on.
        center = [center_x, center_y]
        return center
    
    
    def draw(self, draw, xy, fill):
        """
        Draw the text on an image at the specified location.

        Args:
            draw (ImageDraw.Draw): The drawing context to use for rendering the text.
            xy (tuple): A tuple (x, y) that represents the top-left corner where the text will be drawn.
            fill (tuple): A color value used to fill the text. This can be a tuple representing an RGBA or RGB color.

        Returns:
            None

        Description:
            This method uses the provided drawing context (`draw`) to render the text onto the image at the
            specified position (`xy`). The text is drawn with the color specified in the `fill` argument, and the font defined for the Text object. The `xy` argument determines the starting point for the text, typically the top-left corner of the text.
        """
        draw.text(
            xy,
            self.text,
            fill=fill,
            font=self.font
        )


class PhotoEditor:
    def __init__(self, filename, save_as):
        """
        Initialize a PhotoEditor object.

        Args:
            filename (str): The filename of the image to be edited.
            save_as (str): The filename to save the edited image as.

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
        self.save_as = save_as
        self.photo = Image.open(filename)
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
        transparency = 200
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
        
        author_font_size = 250
        author_text = Text(author, font_path="fonts/georgiai.ttf", font_size=author_font_size)
        
        
        # Get the wrapped text of the author
        wrapped_author_text = author_text.wrap_text(RECTANGLE_WIDTH)
        
        author_transparency = 150
        author_fill = (117, 128, 129, author_transparency)
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
        
        quote_font_size = 250
        
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
        Save the edited photo to the path specified in 'self.save_as'.
        
        Returns:
            None
        """
        self.photo.save(self.save_as)
    
    
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