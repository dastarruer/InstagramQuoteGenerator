from PIL import Image, ImageFont, ImageDraw


filename = "image.JPEG"

class PhotoEditor:
    def __init__(self, photo):
        self.photo = photo
        self.width, self.height = photo.size
        self.draw = ImageDraw.Draw(photo, "RGBA")
        
        # This is the offset of the rectangle that is drawn over the photo for better readability
        rectangle_x_offset = 50
        rectangle_y_offset = 100 
        
        # This is the rectangle 's xy coordinates
        self.rectangle_x0 = rectangle_x_offset
        self.rectanlge_x1 = self.width - rectangle_x_offset
        self.rectangle_y0 = rectangle_y_offset
        self.rectangle_y1 = self.height - rectangle_y_offset
        
    
    def draw_rectangle(self):
        """
        Draw a semi-transparent rectangle over the photo, similar to how quotes are displayed on Instagram. This effect mimics the style where stock photos are paired with a transparent rectangle, and text is written on top of it for better readability.
        """
        xy = (self.rectangle_x0, self.rectangle_y0, self.rectanlge_x1, self.rectangle_y1)
        transparency = 200
        self.draw.rectangle(
            xy = xy, 
            fill = (255, 255, 255, transparency), 
            outline = (255, 255, 255), 
        )
        
    
    def draw_quote(self, quote):
        """
        Draw the quote on top of the photo. It is centered on top of the transparent rectangle that can be drawn with 'draw_rectangle()'.
        """
        font_size = 300
        font = ImageFont.truetype("fonts/georgiaz.ttf", font_size)
        text_width = font.getlength(quote)

        x_center = (self.rectanlge_x1 - self.rectangle_x0 - text_width) // 2
        y_center = (self.rectangle_y1 - self.rectangle_y0) // 2
        position_center = (x_center, y_center)

        self.draw.text(
            position_center,
            quote,
            fill=(0, 0, 0),
            font=font
        )
    
    
    def edit_photo(self, quote):
        """
        Execute both 'draw_rectangle()' and 'draw_quote()'.
        """
        self.draw_rectangle()
        self.draw_quote()
    
    
    def show_photo(self):
        """
        Show the photo.
        """
        self.photo.show()


# Open photo
photo = Image.open(filename)

photo_editor = PhotoEditor(photo)
photo_editor.edit_photo("If the cheetah jumps, so do you.")
photo_editor.show_photo()