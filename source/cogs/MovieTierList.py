import json
import discord
from discord.ext import commands

class MovieTierList(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open('./json/film_list.json', 'r') as f:
            self.films_loaded = json.loads(f.read())

    def __enter__(self):
        return self

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
                "reviewer_id": ctx.message.author.id,
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
    async def maddrev(self, ctx, *, arg = ''):
        self.review_name = self.movie_rev_parse(arg, 1)
        self.review_rate = self.movie_rev_parse(arg, 2)
        self.review_comment = self.movie_rev_parse(arg, 3)
        self.new_commentary = [{
            "reviewer_id": ctx.message.author.id,
            "reviewer_comment": self.review_comment,
            "rate": self.review_rate
        }]
        for i in range(len(self.films_loaded)):
            if self.films_loaded[i]["Name"] == self.review_name:
                for j in range(len(self.films_loaded[i]["Commentary"])):
                    print('\n\ni: {}   j: {}\n\n'.format(i,j))
                    if self.films_loaded[i]["Commentary"][j]["reviewer_id"] == (ctx.message.author.id or ""):
                        self.films_loaded[i]["Commentary"][j]["reviewer_comment"] = self.review_comment
                        self.films_loaded[i]["Commentary"][j]["rate"] = self.review_rate
                        print(self.films_loaded[i]["Commentary"][j]["reviewer_comment"])
                        break
                    elif j == len(self.films_loaded[i]["Commentary"]) - 1:
                        self.films_loaded[i]["Commentary"] += self.new_commentary
                        break
            elif i == len(self.films_loaded) - 1:
                print('{} film was not found\n'.format(self.review_name))
                await ctx.send('Фильм "{}" не был обнаружен. Добавь его с помошью ",madd "!'.format(self.review_name))
                break
        with open('./json/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.films_loaded, sort_keys = False, indent = 2))

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
            f.write(json.dumps(self.films_loaded, sort_keys = False, indent = 2))
        if self.is_deleted:
            print('{} was successfully removed\n'.format(self.name))
            await ctx.send('{} был удалён из списка. И ладно.'.format(self.name))
        else:
            print('{} was not found\n'.format(self.name))
            await ctx.send('{} не найден. Может, его никогда и не было?'.format(self.name))

    def movie_rev_parse(self, name, number):
        self.viewer_parts = name.split("]")
        if number == 1:
            return self.viewer_parts[0]
        elif number == 2:
            return self.viewer_parts[1]
        return self.viewer_parts[2]

def setup(client):
    client.add_cog(MovieTierList(client))