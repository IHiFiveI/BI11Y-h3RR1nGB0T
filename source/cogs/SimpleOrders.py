import os

import discord
import youtube_dl
import shutil
import asyncio
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
    async def slap(self, ctx, *, arg=''):
        if arg == 'bass' or arg == 'BASS':
            await ctx.channel.send(file=discord.File('./images/mystery.png'))
            return
        arg = self.mention_to_id(arg)
        if not arg:
            await ctx.send("SLAPP не удастся....")
            return

        self.slap_channel = ''
        for channel_to_search in ctx.guild.voice_channels:
            for member in channel_to_search.members:
                if member.id == arg:
                    self.slap_channel = member.voice.channel
        if self.slap_channel == '':
            await ctx.send('Некому сделать slapp :(')
            return
        # self.voice = get(self.client.voice_clients, guild=ctx.guild)

        # if self.voice and self.voice.is_connected():
        #     await self.voice.move_to(self.slap_channel)
        # else:
        #     self.voice = await self.slap_channel.connect()

        # self.voice.play(discord.FFmpegPCMAudio('./audio/slap.mp3'))
        # self.voice.source = discord.PCMVolumeTransformer(self.voice.source)
        # self.voice.source.volume = 0.1
        # while not player.is_done():
        #     await asyncio.sleep(1)
        # await ctx.send("Подтверждаю SLAPP")

        # if self.voice and self.voice.is_connected():
        #     await self.voice.disconnect()
        self.vc = await self.slap_channel.connect()
        self.player = vc.create_ffmpeg_player('slap.mp3', after=lambda: print('done'))
        self.player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        self.player.stop()
        await self.vc.disconnect()

    def mention_to_id(self, arg):
        if len(arg) == 22:
            for letter in '<>@!':
                arg = arg.replace(letter, "")
        try:
            arg = int(arg)
        except:
            print('cannot convert argument to int\n')
            arg = 0
        return arg

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
