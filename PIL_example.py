from PIL import Image

import numpy as np

img = Image.open("data_mask_1354_2030.png")

background = Image.open("background_1354_2030.png")

background.paste(img, (0, 0), img)
background.save('how_to_superimpose_two_images_01.png',"PNG")
