import sys
import os
from PIL import Image

# Grab First and Second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if new\ exists, if not create it
# due to the if statement, it won't make duplicate "new" folders once created
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through \image folder and convert images to png
# save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_imagename = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_imagename}.png", 'png')
    print('all done!')
