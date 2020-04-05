import os
from sys import argv
from PIL import Image

# Get path for files new and old one, assume that user puts '/' at the end of argument
path = argv[1]
new_path = argv[2]
#  check if new file exist, if not create it
if not os.path.exists(new_path):
    os.makedirs(new_path)
# loop thro images and split name of image
for image in os.listdir(path):
    # this will pslit text by its name and format in tuple **('filename', '.format')
    file_name = os.path.splitext(image)
    # open image
    image = Image.open(f'{path}{image}')
    # save to the new file
    image.save(f'{new_path}{file_name[0]}.png', 'png')
