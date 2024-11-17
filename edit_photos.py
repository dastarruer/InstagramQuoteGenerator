from PIL import Image

filename = "image.JPEG"
# Open photo
photo = Image.open(filename)

# Save photo
photo.save(filename)
photo.show()