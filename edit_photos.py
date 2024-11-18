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
        
    
    def draw_quote(self, quote, quotee):
        """
        Draw the quote on top of the photo. It is centered in relation to the transparent rectangle that can be drawn with 'draw_rectangle()'.
        """
        rectangle_width = self.rectangle_x1 - self.rectangle_x0
        rectangle_height = self.rectangle_y1 - self.rectangle_y0
        
        quote_font_size = 300
        quote_font = ImageFont.truetype("fonts/georgia.ttf", quote_font_size)
        
        quote_bbox = quote_font.getbbox(quote)
        quote_width = abs(quote_bbox[0] - quote_bbox[2])
        quote_height = abs(quote_bbox[1] - quote_bbox[3])
              
        quote_x = (rectangle_width - quote_width) // 2
        quote_y = (rectangle_height - quote_height) // 2
        quote_xy = (quote_x, quote_y)
        
        quotee_font_size = 250
        quotee_font = ImageFont.truetype("fonts/georgiai.ttf", quotee_font_size)
        
        quotee_bbox = quotee_font.getbbox(quotee)
        quotee_width = abs(quotee_bbox[0] - quotee_bbox[2])
        quotee_height = abs(quotee_bbox[1] - quotee_bbox[3])

        quotee_x = (rectangle_width - quotee_width) // 2
        quotee_y = (quote_y + quote_height / 2) + quotee_height
        quotee_xy = (quotee_x, quotee_y)

        quote_fill = (0, 0, 0)
        quotee_transparency = 150
        quotee_fill = (117, 128, 129, quotee_transparency)
        self.draw.text(
            quote_xy,
            quote,
            fill=quote_fill,
            font=quote_font
        )
        
        self.draw.text(
            quotee_xy,
            quotee,
            fill=quotee_fill,
            font=quotee_font
        )
    
    
    def edit_photo(self, quote, quotee):
        """
        Execute both 'draw_rectangle()' and 'draw_quote()'.
        """
        self.draw_rectangle()
        self.draw_quote(quote, quotee)
    
    
    def show_photo(self):
        """
        Show the photo.
        """
        self.photo.show()


# Open photo
photo = Image.open(filename)

photo_editor = PhotoEditor(photo)
photo_editor.edit_photo("Neque porro quisquam est...", "Me")
photo_editor.show_photo()