from PIL import Image, ImageFont, ImageDraw


filename = "image.JPEG"

class PhotoEditor:
    def __init__(self, photo):
        self.photo = photo
        self.width, self.height = photo.size
        self.draw = ImageDraw.Draw(photo, "RGBA")
        
        x_offset = 50
        y_offset = 100 
        
        self.x0 = x_offset
        self.x1 = self.width - x_offset
        self.y0 = y_offset
        self.y1 = self.height - y_offset
        
    
    def draw_rectangle(self):
        """
        Draw a semi-transparent rectangle over the photo, similar to how quotes are displayed on Instagram. This effect mimics the style where stock photos are paired with a transparent rectangle, and text is written on top of it for better readability.
        """
        xy = (self.x0, self.y0, self.x1, self.y1)
        transparency = 200

        self.draw.rectangle(
            xy = xy, 
            fill = (255, 255, 255, transparency), 
            outline = (255, 255, 255), 
        )
        
    
    def draw_quote(self, quote):
        font_size = 300
        font = ImageFont.truetype("fonts/georgiaz.ttf", font_size)
        text_width = font.getlength(quote)

        x_center = (self.x1 - self.x0 - text_width) // 2
        y_center = (self.y1 - self.y0) // 2
        position_center = (x_center, y_center)

        self.draw.text(
            position_center,
            quote,
            fill=(0, 0, 0),
            font=font
        )
    
    
    def edit_photo(self, quote):
        self.draw_rectangle()
        self.draw_quote()
    
    
    def show_photo(self):
        self.photo.show()


# Open photo
photo = Image.open(filename)

photo_editor = PhotoEditor(photo)
photo_editor.edit_photo("If the cheetah jumps, so do you.")
photo_editor.show_photo()