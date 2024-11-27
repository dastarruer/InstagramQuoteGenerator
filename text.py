from PIL import ImageFont

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