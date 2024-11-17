from PIL import Image, ImageFont, ImageDraw


filename = "image.JPEG"

# Open photo
photo = Image.open(filename)

draw = ImageDraw.Draw(photo, "RGBA")

# Placeholder values until I can dynamically obtain the width and height of the image
width = 6000
height = 4000

x_offset = 50
y_offset = 100 

x0 = x_offset
x1 = width - x_offset
y0 = y_offset
y1 = height - y_offset

xy = (x0, y0, x1, y1)
transparency = 200

draw.rectangle(
    xy = xy, 
    fill = (255, 255, 255, transparency), 
    outline = (255, 255, 255), 
)

# Again, placeholder values
quote = "If a cheetah jumps, so do you."
size = 300
font = ImageFont.truetype("fonts/georgiaz.ttf", size)
text_width = font.getlength(quote)

x_center = (x1 - x0 - text_width) // 2
y_center = (y1 - y0) // 2
position_center = (x_center, y_center)

draw.text(
    position_center,
    quote,
    fill=(0, 0, 0),
    font=font
)

# Show photo
photo.show()