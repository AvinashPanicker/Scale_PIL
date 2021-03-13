#!/usr/bin/python3

from PIL import Image

import os

current = os.getcwd() #current_working_directory

old_path = current + "/"

new_path = "/opt/icons/"

photo_list = os.listdir(old_path) #all the images in /images/

for file_name in photo_list:

  #iterate through all the photos in the lis.

  if not file_name.startswith('.') and not file_name.endswith("py"):
    #condition implemented to get only the image files

    im = Image.open(old_path + file_name)

    new_im = im.resize((128, 128))

    new_im = new_im.convert('RGB')

    new_im = new_im.rotate(-90)

    new_im.save(new_path + file_name , "jpeg")
    #scaling and conversion done.

