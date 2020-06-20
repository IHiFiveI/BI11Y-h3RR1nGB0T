import sys
import random

import json
import cv2
from PIL import Image, ImageDraw, ImageFont

image = Image.open('./source/cogs/temp/file.png')
draw = ImageDraw.Draw(image)

with open('./json/wolf_quotes.json', 'r', encoding='UTF-8') as f:
    qoutes = json.loads(f.read())
text = random.choice(qoutes)
font = ImageFont.truetype('./fonts/comicbd.ttf', size=72, encoding='UTF-8')

text_width, text_height = draw.textsize(text, font=font)
x_pos = image.size[0] * 0.5 - text_width * 0.5
y_pos = 90 - text_height * 0.5

i = 0
while i < 6:
    y_add = 5 if i < 3 else -5
    x_add = 5 if not (i & 1) else -5
    if i == 4 or not i:
        x_add = 0

    draw.text((x_pos + x_add, y_pos + y_add), text, fill='rgb(0,0,0)', font=font, align="center")
    i += 1

draw.text((x_pos, y_pos), text, fill='rgb(255,255,255)', font=font, align="center")
image.save('./source/cogs/temp/file1.png', format=None)
