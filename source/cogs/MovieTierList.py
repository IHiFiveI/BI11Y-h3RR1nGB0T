import json
import discord
from discord.ext import commands

class MovieTierList(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open('./json/film_list.json', 'r') as f:
            self.films_loaded = json.loads(f.read())

    @commands.command()
    async def mlist(self, ctx):
        self.list = 'Список просмотренных фильмов:\n'
        for film in self.films_loaded:
            self.list += film['Name'] + "\n"
        await ctx.send(self.list)

    @commands.command()
    async def madd(self, ctx, arg = ''):
        self.new_info = [{
            "Name": arg,
            "Commentary":[
                {
                "reviewer_id": "",
                "reviewer_comment": "",
                "rate": "0"
                }
            ]
        }]
        self.films_loaded += self.new_info
        with open('./json/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.films_loaded, sort_keys = False, indent = 2))

def setup(client):
    client.add_cog(MovieTierList(client))