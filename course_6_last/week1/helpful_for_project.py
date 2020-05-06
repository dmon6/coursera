#!/usr/bin/env python3.7
'''
Example usages of PIL
'''
import os
from PIL import Image
image_file = ''
im = Image.open(image_file)

im.rotate(45).show()
im.resize(640, 480)
im.save('new_file.jpg')

# You can also do it like

files_to_modify = [picture for picture in os.listdir('.') if '.png' in picture]


def do_stuff_to_picture(picture):
    new_im = Image(picture)
    return new_im.rotate(180).resize(640, 480).save(picture + '.jpg')


file_format = '.jpg'
img_res = '128,128'
rotation = 90


>> > def modify_shit(picture):
...     img = Image.open(picture)
...     img2 = img.rotate(90).resize((128, 128)).convert("RGB")
...     img2.save('test_folder/' + picture + '.jpg')
...
