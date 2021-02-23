#!/usr/bin/env python3

import os
from PIL import Image

#user input for source folder, make sure directory ends with /
source = input("Input source directory here: ")

#creates list of images in folder to run through with for loop
images = os.listdir(source)

#user input for destination folder, make sure directory ends with /
destination = input("Input destination directory here: ")

for image in images:
  if not image.startswith('.'):
    #open image
    img = Image.open(source + image)
    #convert image to RGB
    img = img.convert('RGB')
    #rotate image 90 degrees clockwise
    img = img.rotate(-90)
    #resize image to 128 X 128
    img = img.resize((128, 128))
    #save image to new file in .jpeg format in destination folder
    img = img.save(destination +  image, 'jpeg')
