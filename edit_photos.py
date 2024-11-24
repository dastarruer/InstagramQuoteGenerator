from PIL import Image, ImageFont, ImageDraw


class Text:
    def __init__(self, text: str, font: ImageFont):
        self.text = text
        self.font = font
    
    
    @property
    def width(self):
        bbox = self.font.getbbox(self.text)
        width = abs(bbox[0] - bbox[2])
        return width
    
    
    @property
    def height(self):
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
        current_line = Text("", self.font)
        
        for word in words:
            # Store the current word as a Text object, adding a trailing space
            # Without the trailing space, the line 'Who am I?' would instead become 'WhoamI?'
            word = Text(word + " ", self.font)
            if word.width + current_line.width >= max_width:
                # If 'line' was set to 'current_line', any changes made to 'current_line' would also be applied to 'line'. 
                # So, we have to make an entirely new object.
                line = Text(current_line.text, self.font)
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
        Draw the text on .
        """
        draw.text(
            xy,
            self.text,
            fill=fill,
            font=self.font
        )


class PhotoEditor:
    def __init__(self, filename, save_as):
        self.save_as = save_as
        self.photo = Image.open(filename)
        self.width, self.height = self.photo.size
        self.draw = ImageDraw.Draw(self.photo, "RGBA")
        
        # This is the offset of the rectangle that is drawn over the photo for better readability
        rectangle_x_offset = 50
        rectangle_y_offset = 100 
        
        # This is the rectangle 's xy coordinates
        self.rectangle_x0 = rectangle_x_offset
        self.rectangle_x1 = self.width - rectangle_x_offset
        self.rectangle_y0 = rectangle_y_offset
        self.rectangle_y1 = self.height - rectangle_y_offset
        
    
    def draw_rectangle(self):
        """
        Draw a semi-transparent rectangle over the photo, similar to how quotes are displayed on Instagram. This effect mimics the style where stock photos are paired with a transparent rectangle, and text is written on top of it for better readability.
        """
        xy = (self.rectangle_x0, self.rectangle_y0, self.rectangle_x1, self.rectangle_y1)
        transparency = 200
        self.draw.rectangle(
            xy = xy, 
            fill = (255, 255, 255, transparency), 
            outline = (255, 255, 255), 
        )
        
    
    def draw_quote(self, quote, author):
        """
        Draw the quote on top of the photo. It is centered in relation to the transparent rectangle that can be drawn with 'draw_rectangle()'.
        """
        rectangle_width = self.rectangle_x1 - self.rectangle_x0
        rectangle_height = self.rectangle_y1 - self.rectangle_y0
        
        quote_font_size = 250
        quote_font = ImageFont.truetype("fonts/georgia.ttf", quote_font_size)
        quote_text = Text(quote, quote_font)
        
        quote_fill = (0, 0, 0)
        wrapped_quote_text = quote_text.wrap_text(rectangle_width)
        padding = 20
        for i, line in enumerate(wrapped_quote_text):
            middle = len(wrapped_quote_text) // 3
            line_xy = line.get_center_coordinates(rectangle_width, rectangle_height)
            line_xy[0] += 50
            line_xy[1] -= line.height * (i - middle) + (padding * (i - middle))
            line.draw(self.draw, line_xy, quote_fill)
                
        author_font_size = 250
        author_font = ImageFont.truetype("fonts/georgiai.ttf", author_font_size)
        author_text = Text("- " + author, author_font)

        author_xy = author_text.get_center_coordinates(rectangle_width, rectangle_height)
        
        # Offset the author's y position by the quote's height and a bit of padding
        padding = 30
        author_xy[1] += quote_text.height * 3 + padding

        author_transparency = 150
        author_fill = (117, 128, 129, author_transparency)
        author_text.draw(self.draw, author_xy, author_fill)
    
    
    def save_photo(self):
        """
        Save the photo.
        """
        self.photo.save(self.save_as)
    
    
    def edit_photo(self, quote, author):
        """
        Execute both 'draw_rectangle()' and 'draw_quote()', and save the Image to 'file'.
        """
        self.draw_rectangle()
        self.draw_quote(quote, author)
        self.save_photo()

filename = "static/image.JPEG"
save_as = "static/edited_image.JPEG"
p = PhotoEditor(filename, save_as)
p.edit_photo("Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking.", "Steve Jobs")