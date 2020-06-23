import sys
import os
import random

import discord
from discord.ext import commands
import json
import requests
import shutil
# import cv2
from PIL import Image, ImageDraw, ImageFont


class WolfQuotes(commands.Cog):

    def __init__(self, client):
        self.font_size = 0
        self.client = client
        with open('./json/wolf_quotes.json', 'r', encoding='UTF-8') as f:
            self.qoutes = json.loads(f.read())

    def download_image(self, url='https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg'):
        self.file_name = url.split('/')[-1]
        self.req = requests.get(url, stream=True)
        if self.req.status_code == 200:
            self.req.raw.decode_content = True
            with open('./images/' + self.file_name, 'wb') as f:
                shutil.copyfileobj(self.req.raw, f)
                print('image {} downloaded successfully\n'.format(self.file_name))
        else:
            print('access to image {} cant be granted\n'.format(self.file_name))

    @commands.command()
    async def wolf(self, ctx):
        try:
            self.download_image(ctx.message.attachments[0].url)
        except:
            await ctx.send('Прикрепи картинку то хоть')
        await ctx.channel.purge(limit=1)

        self.file_name = ctx.message.attachments[0].url.split('/')[-1]
        self.image = Image.open('./images/' + self.file_name)
        self.draw = ImageDraw.Draw(self.image)

        self.font_to_img_size = [
            {
                "resolution": 100,
                "size_of_font": 8,
                "how_much_to_add": 1
            },
            {
                "resolution": 300,
                "size_of_font": 20,
                "how_much_to_add": 2
            },
            {
                "resolution": 600,
                "size_of_font": 30,
                "how_much_to_add": 3
            },
            {
                "resolution": 900,
                "size_of_font": 48,
                "how_much_to_add": 4
            },
            {
                "resolution": 1200,
                "size_of_font": 72,
                "how_much_to_add": 5
            },
            {
                "resolution": 1900,
                "size_of_font": 96,
                "how_much_to_add": 6
            },
            {
                "resolution": 2600,
                "size_of_font": 122,
                "how_much_to_add": 7
            },
            {
                "resolution": 3700,
                "size_of_font": 176,
                "how_much_to_add": 8
            }
        ]

        for position in self.font_to_img_size:
            if self.image.size[0] >= position["resolution"]:
                self.font_size = position["size_of_font"]
                self.absolute_add = position["how_much_to_add"]
            else:
                break

        if not self.font_size:
            await ctx.send('Картинка настолько мелкая, что ни один волк не различит')
            os.remove('./images/' + self.file_name)
            return

        self.text = random.choice(self.qoutes)
        self.font = ImageFont.truetype('./fonts/comicbd.ttf', size=self.font_size, encoding='UTF-8')
        self.text_width, self.text_height = self.draw.textsize(self.text, font=self.font)

        self.x_pos = self.image.size[0] * 0.5 - self.text_width * 0.5
        self.y_pos = self.text_height * 0.2

        i = 0
        while i < 6:
            self.y_add = self.absolute_add if i < 3 else -self.absolute_add
            self.x_add = self.absolute_add if not (i & 1) else -self.absolute_add
            if i == 4 or not i:
                self.x_add = 0

            self.draw.text((self.x_pos + self.x_add, self.y_pos + self.y_add), self.text,
                           fill='rgb(0,0,0)', font=self.font, align="center")
            i += 1

        self.draw.text((self.x_pos, self.y_pos), self.text, fill='rgb(255,255,255)',
                       font=self.font, align="center")
        self.image.save('./images/' + 'wolk\'ed_' + self.file_name, format=None)

        await ctx.channel.send(file=discord.File('./images/' + 'wolk\'ed_' + self.file_name))

        os.remove('./images/' + 'wolk\'ed_' + self.file_name)
        os.remove('./images/' + self.file_name)


def setup(client):
    client.add_cog(WolfQuotes(client))
