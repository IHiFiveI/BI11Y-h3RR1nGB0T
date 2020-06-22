import os

import discord
import youtube_dl
import shutil
from discord.ext import commands
from discord.utils import get

from main import is_permission_granted


class SimpleOrders(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.pongCount = 0
        self.pongEnding = '!'
        self.players = {}

    @commands.command()
    async def clear(self, ctx, arg=1):
        if is_permission_granted(ctx.message.author.id):
            await ctx.channel.purge(limit=arg + 1)
        else:
            await ctx.channel.send('Отказано')

    @commands.command(pass_context=True, aliases=['slapp', 's'])
    async def slap(self, ctx, *, arg):
        self.voice = get(self.client.voice_clients, guild=ctx.guild)
        self.channel = ctx.message.author.voice.channel
        if self.voice and self.voice.is_connected():
            await self.voice.move_to(self.channel)
        else:
            self.voice = await self.channel.connect()

        self.voice.play(discord.FFmpegPCMAudio('./audio/Rhythm_Changes.mp3'))
        self.voice.source = discord.PCMVolumeTransformer(voice.source)
        self.voice.source.volume = 0.07

        await ctx.send("Slapped")

        if self.voice and self.voice.is_connected():
            await self.voice.disconnect()

    @commands.command()
    async def help(self, ctx, *, arg=''):
        if arg == 'tech':
            await ctx.send(':wrench: Технические команды :tools:\n'
                           '(доступно лишь админимтраторам; не выводят ничего в чат)\n'
                           '```\n'
                           ',clear (число от 0 до 100)'
                           '\n```'
                           '- очистка чата на указанное количество сообщений (по дефолту одно)\n'
                           '```\n'
                           ',load (название расширения)'
                           '\n```'
                           '- загрузка выбранного расширения. На самом деле, только Пятый и знает их названия\n'
                           '```\n'
                           ',unload (название расширения)'
                           '\n```'
                           '- отключение выбранного расширения.\n'
                           '```\n'
                           ',reload (название расширения)'
                           '\n```'
                           '- перезагрузка выбранного расширения.\n'
                           )
        else:
            await ctx.send('Вот список команд которыми вы можете пользоваться:\n'
                           '(для написания команды используй "," (ну как в майнкрафте была "/" ну вы поняли))\n\n\n'
                           ':film_frames: Блок фильмов: :film_frames:\n'
                           '```\n'
                           ',madd (название фильма)'
                           '\n```'
                           '- добавить фильм по шаблону: название ] оценка(из 10) ] комментарий\n'
                           'просто не спрашивайте почему "]" (если вам вдруг не удобно, то скажите, я поправлю)\n'
                           '```\n'
                           ',maddrev (название фильма)'
                           '\n```'
                           '- добавить/изменить обзор на фильм в списке. Шаблон всё тот же\n'
                           '```\n'
                           ',mrm (название фильма)'
                           '\n```'
                           '- удалить фильм из списка (со всеми обзорами!!!), от шаблона выше требуется только название\n'
                           '```\n'
                           ',mlist'
                           '\n```'
                           '- посмотреть список добавленных фильмов\n'
                           '```\n'
                           ',mstat (название фильма)'
                           '\n```'
                           '- посмотреть обзоры на фильм по названию\n\n\n'
                           ':parking::information_source: Блок всякой хероты: :sos:\n'
                           '```\n'
                           ',ping'
                           '\n```'
                           '- никита зачем\n'
                           'гигант программирования отец русского python`а\n'
                           '```\n'
                           ',slap (упоминание на сервере)'
                           '\n```'
                           '- :male_sign:никита:male_sign:зачем:male_sign:\n'
                           '",slap @I_Hi_Five_I#9085"\n\n'
                           'Хотите видеть больше? Я писал это 4 недели хз ну вообще слушаю ваши предложения'
                           )

    @commands.command()
    async def ping(self, ctx):
        if self.pongCount == 4:
            await ctx.send('you knew, im getting tired')
        elif self.pongCount == 6:
            self.pongEnding = ""
        elif self.pongCount == 13:
            await ctx.send('can you stop, please?')
            self.pongEnding = "."
        elif self.pongCount == 16:
            await ctx.send('ok bye retards i dont want to play with you anymore')
            await self.client.close()
        try:
            await ctx.send('pong' + self.pongEnding)
            self.pongCount += 1
        except:
            print('bot was ping-ponged out of existance\n')


def setup(client):
    client.add_cog(SimpleOrders(client))
