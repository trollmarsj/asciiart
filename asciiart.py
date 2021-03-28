import sys, random, argparse
import numpy as np
import math

from PIL import Image

# define greyscale level
# 70 level greyscale
gscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 level greyscale
gscale10 = "@%#*+=-:. "

def convertImageToAscii(fileName, cols, scale):
    # open image and convert to greyscale
    image = Image.open(fileName).convert("L")
    # size of image
    W, H = image.size[0], image.size[1]
    print("image dimension %d * %d" %(W, H))

    # unit width
    w = W / cols
    # unit height based on scale
    h = w / scale
    rows = int(H / h)

    if W < cols or H < rows:
        print("image is too small for specified cols!")
        exit(0)

    aimg = []



if __name__ == "__main__":
    convertImageToAscii()