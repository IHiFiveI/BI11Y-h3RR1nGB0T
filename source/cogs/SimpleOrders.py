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

    @commands.command(pass_context=True, aliases=['pryamo', 'ahd'])
    async def ahead(self, ctx, *, arg=''):
        persons_id = self.mention_to_id(arg)
        if not persons_id:
            return

        await ctx.send("Прямо дикий <@!{}>!".format(persons_id))
        await self.sound_play(ctx, persons_id, 'scav_ahead', 'Никого не вижу...')

    @commands.command(pass_context=True, aliases=['slapp'])
    async def slap(self, ctx, *, arg=''):
        if arg == 'bass' or arg == 'BASS':
            await ctx.channel.send(file=discord.File('./images/mystery.png'))
            return
        persons_id = self.mention_to_id(arg)
        if not persons_id:
            await ctx.send("SLAPP не удастся....")
            return

        await self.sound_play(ctx, persons_id, 'slap', 'Некому сделать slapp :(')

        await ctx.send("Подтверждаю SLAPP")

    async def sound_play(self, ctx, persons_id, sound_name, error_text):
        self.mentioned_persons_channel = ''
        for channel_to_search in ctx.guild.voice_channels:
            for member in channel_to_search.members:
                if member.id == persons_id:
                    self.mentioned_persons_channel = member.voice.channel
        if self.mentioned_persons_channel == '':
            await ctx.send(error_text)
            return

        self.voice = get(self.client.voice_clients, guild=ctx.guild)
        if self.voice and self.voice.is_connected():
            await self.voice.move_to(self.mentioned_persons_channel)
        else:
            self.voice = await self.mentioned_persons_channel.connect()

        self.voice.play(discord.FFmpegPCMAudio('./audio/{}.mp3'.format(sound_name)))
        self.voice.source = discord.PCMVolumeTransformer(self.voice.source)
        self.voice.source.volume = 0.6
        while self.voice.is_playing():
            await asyncio.sleep(1)

        if self.voice and self.voice.is_connected():
            await self.voice.disconnect()

    def mention_to_id(self, arg):
        if len(arg) == 22:
            for letter in '<>@!':
                arg = arg.replace(letter, "")
        try:
            arg = int(arg)
        except:
            print('"{}" cannot be converted to int\n'.format(arg))
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
                           '- паскаль информатика 3 класс горячев горина суворова гдз\n'
                           '```\n'
                           ',slap (упоминание на сервере)'
                           '\n```'
                           '- :male_sign:\n'
                           '```\n'
                           ',ahead (упоминание на сервере)'
                           '\n```'
                           '- сообщить товарищам о присутствии кого-то рядом\n'
                           )

    @commands.command()
    async def ping(self, ctx):
        if self.pongCount == 4:
            await ctx.send('you know, im getting tired')
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
