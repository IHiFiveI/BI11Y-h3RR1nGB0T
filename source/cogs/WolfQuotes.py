import sys
import random

import discord
from discord.ext import commands
import json
import cv2
from PIL import Image, ImageDraw, ImageFont


class WolfQuotes(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open('./json/wolf_quotes.json', 'r', encoding='UTF-8') as f:
            self.qoutes = json.loads(f.read())
        self.image = Image.open('./images/file.png')
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype('./fonts/comicbd.ttf', size=72, encoding='UTF-8')

    @commands.command()
    async def wolf(self, ctx):
        self.text = random.choice(self.qoutes)

        self.text_width, self.text_height = self.draw.textsize(self.text, font=self.font)
        self.x_pos = self.image.size[0] * 0.5 - self.text_width * 0.5
        self.y_pos = 90 - self.text_height * 0.5

        i = 0
        while i < 6:
            self.y_add = 5 if i < 3 else -5
            self.x_add = 5 if not (i & 1) else -5
            if i == 4 or not i:
                self.x_add = 0

            self.draw.text((self.x_pos + self.x_add, self.y_pos + self.y_add), self.text,
                           fill='rgb(0,0,0)', font=self.font, align="center")
            i += 1

        self.draw.text((self.x_pos, self.y_pos), self.text, fill='rgb(255,255,255)',
                       font=self.font, align="center")
        self.image.save('./images/file1.png', format=None)


def setup(client):
    client.add_cog(WolfQuotes(client))
