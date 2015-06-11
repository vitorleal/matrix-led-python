#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

# 8-bit paletted GIF scrolling example
image = Image.open("cloud.gif")
image.load()          # Must do this before SetImage() calls
matrix.Fill(0x6F85FF) # Fill screen to sky color
for n in range(32, -image.size[0], -1): # Scroll R to L
	matrix.SetImage(image.im.id, n, 0)
	time.sleep(0.025)

matrix.Clear()
