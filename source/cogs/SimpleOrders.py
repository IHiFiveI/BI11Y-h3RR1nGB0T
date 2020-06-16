import discord
from discord.ext import commands

from main import is_permission_granted

class SimpleOrders(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.pongCount = 0
        self.pongEnding = '!'

    @commands.command()
    async def clear(self, ctx, arg = 1):
        if is_permission_granted(ctx.message.author.id):
            await ctx.channel.purge(limit = arg + 1)
        else:
            await ctx.channel.send('Отказано')

    @commands.command()
    async def help(self, ctx):
        await ctx.send('Вот список команд которыми вы можете пользоваться:\n'
                       '(для написания команды используй "," (ну как в майнкрафте была "/" ну вы поняли))\n\n\n'
                       ':film_frames: Блок фильмов: :film_frames:\n'
                       '```\n'
                       ',madd'
                       '\n```'
                       '- добавить фильм по шаблону: название ] оценка(из 10) ] комментарий\n'
                       'просто не спрашивайте почему "]" (если вам вдруг не удобно, то скажите, я поправлю)\n'
                       '```\n'
                       ',maddrev'
                       '\n```'
                       '- добавить/изменить обзор на фильм в списке. Шаблон всё тот же\n'
                       '```\n'
                       ',mrm'
                       '\n```'
                       '- удалить фильм из списка (со всеми обзорами!!!), от шаблона выше требуется только название\n'
                       '```\n'
                       ',mlist'
                       '\n```'
                       '- посмотреть список добавленных фильмов\n'
                       '```\n'
                       ',mstat'
                       '\n```'
                       '- посмотреть обзоры на фильм по названию\n\n\n'
                       ':parking::information_source: Блок всякой хероты: :sos:\n'
                       '```\n'
                       ',ping'
                       '\n```'
                       '- никита зачем\n'
                       'гигант программирования отец русского python`а\n'
                       '```\n'
                       ',slap'
                       '\n```'
                       '- :male_sign:никита:male_sign:зачем:male_sign:\n'
                       'принимает аргументом человека на сервере типо ",slap @I_Hi_Five_I#9085"\n\n'
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