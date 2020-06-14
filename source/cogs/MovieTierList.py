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
    async def madd(self, ctx, *, arg = ''):
        self.name = self.movie_rev_parse(arg, 1)
        self.new_info = [{
            "Name": self.name,
            "Commentary":[
                {
                "reviewer_id": "",
                "reviewer_comment": self.movie_rev_parse(arg, 3),
                "rate": self.movie_rev_parse(arg, 2)
                }
            ]
        }]
        self.films_loaded += self.new_info
        with open('./json/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.films_loaded, sort_keys = False, indent = 2))
        print('{} was successfully added\n'.format(self.name))
        await ctx.send('{} добавлен в список'.format(self.name))

    @commands.command()
    async def mrm(self, ctx, *, arg = ''):
        self.is_deleted = False
        self.name = self.movie_rev_parse(arg, 1)
        for i in range(len(self.films_loaded)):
            if self.films_loaded[i]["Name"] == self.name:
                self.films_loaded.pop(i)
                self.is_deleted = True
                break
        with open('./json/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.films_loaded, sort_keys=False, indent=2))
        if self.is_deleted:
            print('{} was successfully removed\n'.format(self.name))
            await ctx.send('{} был удалён из списка. И ладно.'.format(self.name))
        else:
            print('{} was not found\n'.format(self.name))
            await ctx.send('{} не найден. Может, его никогда и не было?'.format(self.name))

    def movie_rev_parse(self, name, number):
        self.viewer_parts = name.split("\\")
        if number == 1:
            return self.viewer_parts[0]
        elif number == 2:
            return self.viewer_parts[1]
        return self.viewer_parts[2]

def setup(client):
    client.add_cog(MovieTierList(client))