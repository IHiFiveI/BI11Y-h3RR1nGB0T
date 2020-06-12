import json
import discord
from discord.ext import commands

class MovieTierList(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.films_to_write = None
        # with open('./json/film_list.json', 'w', encoding="utf-8") as f:
        #     f.write(json.dumps(self.films_to_write, sort_keys=False, indent=2))
        with open('./json/film_list.json', 'r') as f:
            self.films_loaded = json.loads(f.read())

    @commands.command()
    async def mlist(self, ctx):
        self.list = 'Список просмотренных фильмов:\n'
        for film in self.films_loaded:
            self.list += film['Name'] + "\n"
        await ctx.send(self.list)

    @commands.command()
    async def madd(self, ctx, arg):
        pass

def setup(client):
    client.add_cog(MovieTierList(client))