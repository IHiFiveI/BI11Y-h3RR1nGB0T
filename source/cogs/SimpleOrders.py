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

    @commands.command(pass_context=True, aliases=['cls'])
    async def clear(self, ctx, arg=1):
        if is_permission_granted(ctx.message.author.id) and arg <= 100:
            await ctx.channel.purge(limit=arg + 1)
        else:
            await ctx.channel.send('Отказано')

    @commands.command(pass_context=True, aliases=['slapp', 's'])
    async def slap(self, ctx, *, arg=''):
        # checking arguments
        if arg == ('🅱️ass' or 'bass' or 'BASS'):
            await ctx.channel.send(file=discord.File('./images/mystery.png'))
            return
        arg = self.mention_to_id(arg)
        if arg == 715445878395240470:
            await ctx.channel.send('Нет-нет-нет, дружок-пирожок')
            return
        elif not arg:
            await ctx.send("SLAPP не удастся....")
            return
        #needs to be rewritten into other function
        # finding channel
        self.slap_channel = ''
        for channel_to_search in ctx.guild.voice_channels:
            for member in channel_to_search.members:
                if member.id == arg:
                    self.slap_channel = member.voice.channel
        if self.slap_channel == '':
            await ctx.send('Некому сделать slapp :(')
            return
        # joining channel
        self.voice = get(self.client.voice_clients, guild=ctx.guild)
        if self.voice and self.voice.is_connected():
            await self.voice.move_to(self.slap_channel)
        else:
            self.voice = await self.slap_channel.connect()
        # playing sound
        self.voice.play(discord.FFmpegPCMAudio('./audio/slap.mp3'))
        self.voice.source = discord.PCMVolumeTransformer(self.voice.source)
        self.voice.source.volume = 0.6
        while self.voice.is_playing():
            await asyncio.sleep(1)
        await ctx.send("Подтверждаю SLAPP")
        # disconnecting
        if self.voice and self.voice.is_connected():
            await self.voice.disconnect()

    def mention_to_id(self, arg):
        # id that taken from mention looks like '<@!id>', when id - 18 letters long string 
        # removing unnecessary symbols from parsed string
        if len(arg) == 22:
            for letter in '<>@!':
                arg = arg.replace(letter, "")
        # string to int convertation
        try:
            arg = int(arg)
        except:
            print('cannot convert argument to int\n')
            arg = 0

        return arg

    @commands.command(pass_context=True, aliases=['halp'])
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
            await ctx.send('Вот список доступных на данный момент команд:\n\n\n'
                           ':film_frames: Блок фильмов: :film_frames:\n'
                           '```\n'
                           ',madd (название фильма)'
                           '\n```'
                           '- добавить фильм по шаблону: название ] оценка(из 10) ] комментарий\n'
                           'просто не спрашивайте почему "]" (но если не удобно, скажите)\n'
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
                           ':parking: Блок всякой хероты: :parking:\n'
                           '```\n'
                           ',help (необязательный аргумент)'
                           '\n```'
                           '- выводит это сообщение. Используй ",help tech" для отображения технических команд\n'
                           '```\n'
                           ',ping'
                           '\n```'
                           '- никита зачем\n'
                           '```\n'
                           ',slap (упоминание на сервере)'
                           '\n```'
                           '- :male_sign:никита:male_sign:зачем:male_sign:\n\n'
                           )

    @commands.command()
    async def ping(self, ctx):
        if self.pongCount == 4:
            await ctx.send('знаешь, я начинаю уставать')
        elif self.pongCount == 6:
            self.pongEnding = ""
        elif self.pongCount == 13:
            await ctx.send('может прекратим, пожалуйста?')
            self.pongEnding = "."
        elif self.pongCount == 16:
            await ctx.send('ладно ретарды всем пока я не буду с вами играть больше')
            await self.client.close()
        try:
            await ctx.send('pong' + self.pongEnding)
            self.pongCount += 1
        except:
            print('bot was ping-ponged out of existance\n')


def setup(client):
    client.add_cog(SimpleOrders(client))
