#!/usr/bin/env python3
from PIL import Image

im = Image.open("example.jpg")
half_width=int(im.size[0]/2)
half_height=int(im.size[1]/2)
new_im = im.resize((half_width,half_height))
new_im.save("example_resized.jpg")


im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")


im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
