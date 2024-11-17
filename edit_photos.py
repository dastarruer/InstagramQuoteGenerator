from PIL import Image, ImageDraw


filename = "image.JPEG"

# Open photo
photo = Image.open(filename)

draw = ImageDraw.Draw(photo)

# Placeholder values until I can dynamically obtain the width and height of the image
width = 4845
height = 3484

x_offset = 50
y_offset = 100 

x0 = x_offset
x1 = width - x_offset
y0 = y_offset
y1 = height - y_offset
xy = (x0, y0, x1, y1)

draw.rectangle(
    xy = xy, 
    fill = (255, 255, 255, 50), 
    outline = (255, 255, 255), 
)

# Show photo
photo.show()