import json
import discord
import os
from discord.ext import commands


class MovieTierList(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.servers_own_films = ""
        self.server_data_path = ""

    def get_guild(self, arg = 0):
        self.server_data_path = './json/{}'.format(arg)

        if not os.path.exists(self.server_data_path):
            os.mkdir(self.server_data_path)
            with open(self.server_data_path + '/film_list.json', 'w') as fp:
                fp.write('[\n]')
        with open(self.server_data_path + '/film_list.json', 'r') as f:
            self.films_loaded = json.loads(f.read())

        return self.films_loaded

    @commands.command()
    async def mlist(self, ctx):
        self.servers_own_films = self.get_guild(ctx.message.guild.id)
        self.list = 'Список просмотренных фильмов:\n\n'
        for film in self.servers_own_films:
            self.list += film['Name'] + "\n"
        if self.list != 'Список просмотренных фильмов:\n\n':
            await ctx.send(self.list)
        else:
            await ctx.send('Список пуст.')

    @commands.command()
    async def madd(self, ctx, *, arg=''):
        self.servers_own_films = self.get_guild(ctx.message.guild.id)
        self.name = self.movie_rev_parse(arg, 1)
        self.new_info = [{
            "Name": self.name,
            "Commentary": [
                {
                    "reviewer_id": ctx.message.author.id,
                    "reviewer_comment": self.movie_rev_parse(arg, 3),
                    "rate": self.movie_rev_parse(arg, 2)
                }
            ]
        }]
        self.servers_own_films += self.new_info
        with open('./json/{}'.format(ctx.message.guild.id) + '/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.servers_own_films, sort_keys=False, indent=2))
        print('{} was successfully added\n'.format(self.name))
        await ctx.send('{} добавлен в список'.format(self.name))

    @commands.command()
    async def maddrev(self, ctx, *, arg=''):
        self.servers_own_films = self.get_guild(ctx.message.guild.id)
        self.review_name = self.movie_rev_parse(arg, 1)
        self.review_rate = self.movie_rev_parse(arg, 2)
        self.review_comment = self.movie_rev_parse(arg, 3)
        self.new_commentary = [{
            "reviewer_id": ctx.message.author.id,
            "reviewer_comment": self.review_comment,
            "rate": self.review_rate
        }]
        for i in range(len(self.servers_own_films)):
            if self.servers_own_films[i]["Name"] == self.review_name:
                for j in range(len(self.servers_own_films[i]["Commentary"])):
                    if self.servers_own_films[i]["Commentary"][j]["reviewer_id"] == (ctx.message.author.id or ""):
                        self.servers_own_films[i]["Commentary"][j][
                            "reviewer_comment"] = self.review_comment
                        self.servers_own_films[i]["Commentary"][j]["rate"] = self.review_rate
                        break
                    elif j == len(self.servers_own_films[i]["Commentary"]) - 1:
                        self.servers_own_films[i]["Commentary"] += self.new_commentary
                        break
            elif i == len(self.servers_own_films) - 1:
                print('{} film was not found\n'.format(self.review_name))
                await ctx.send('Фильм "{}" не был обнаружен. Добавь его с помошью ",madd"!'.format(self.review_name))
                break
        with open('./json/{}'.format(ctx.message.guild.id) + '/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.servers_own_films, sort_keys=False, indent=2))

    @commands.command()
    async def mrm(self, ctx, *, arg=''):
        self.servers_own_films = self.get_guild(ctx.message.guild.id)
        self.is_deleted = False
        self.name = self.movie_rev_parse(arg, 1)
        for i in range(len(self.servers_own_films)):
            if self.servers_own_films[i]["Name"] == self.name:
                self.servers_own_films.pop(i)
                self.is_deleted = True
                break
        with open('./json/{}'.format(ctx.message.guild.id) + '/film_list.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.servers_own_films, sort_keys=False, indent=2))
        if self.is_deleted:
            print('{} was successfully removed\n'.format(self.name))
            await ctx.send('{} был удалён из списка. И ладно.'.format(self.name))
        else:
            print('{} was not found\n'.format(self.name))
            await ctx.send('{} не найден. Может, его никогда и не было?'.format(self.name))

    @commands.command()
    async def mstat(self, ctx, *, arg=''):
        self.servers_own_films = self.get_guild(ctx.message.guild.id)
        self.review_name = self.movie_rev_parse(arg, 1)
        self.comment_to_show = ''
        for i in range(len(self.servers_own_films)):
            if self.servers_own_films[i]["Name"] == self.review_name:
                for j in range(len(self.servers_own_films[i]["Commentary"])):
                    try:
                        self.comment_to_show += '```\nОбзорщик: ' + str(await self.client.fetch_user(self.servers_own_films[i]["Commentary"][j]["reviewer_id"]))
                    except:
                        self.comment_to_show += '```\nОбзорщик: Неизвестный'
                    self.comment_to_show += '\nОценка: ' + \
                        self.servers_own_films[i]["Commentary"][j]["rate"]
                    self.comment_to_show += '\\10\nКомментарий: ' + \
                        self.servers_own_films[i]["Commentary"][j]["reviewer_comment"]
                    self.comment_to_show += '\n```'
        if arg == '':
            print('blank line was entered as an arg\n')
            await ctx.send('Аргументом введена пустая строка')
            return
        if self.comment_to_show == '':
            print('{} film was not found\n'.format(self.review_name))
            await ctx.send('Фильм "{}" не был обнаружен'.format(self.review_name))
            return
        await ctx.send(':film_frames:Обзор на ' + self.review_name + ':')
        await ctx.send(self.comment_to_show)

    def movie_rev_parse(self, name, number):
        self.viewer_parts = name.split("]")
        if number == 1:
            return self.viewer_parts[0]
        elif number == 2:
            return self.viewer_parts[1]
        return self.viewer_parts[2]


def setup(client):
    client.add_cog(MovieTierList(client))
