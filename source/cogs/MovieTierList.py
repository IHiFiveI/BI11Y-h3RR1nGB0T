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
        self.list = 'Список просмотренных фильмов:\n\n'
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
        print('{} was successfully added\n'.format(arg))
        await ctx.send('{} добавлен в список'.format(arg))

    @commands.command()
    async def mrm(self, ctx, arg = ''):
        self.is_deleted = False
        for i in range(len(self.films_loaded)):
            if self.films_loaded[i]["Name"] == arg:
                self.films_loaded.pop(i)
                self.is_deleted = True
                break
        with open('./json/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.films_loaded, sort_keys=False, indent=2))
        if self.is_deleted:
            print('{} was successfully removed\n'.format(arg))
            await ctx.send('{} был удалён из списка. И ладно.'.format(arg))
        else:
            print('{} was not found\n'.format(arg))
            await ctx.send('{} не найден. Может, его никогда и не было?'.format(arg))


def setup(client):
    client.add_cog(MovieTierList(client))