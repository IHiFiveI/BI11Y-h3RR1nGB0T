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
        print(ctx.message.author.id)
        if is_permission_granted(ctx, ctx.message.author.id):
            await ctx.channel.purge(limit = arg + 1)
        else:
            await ctx.channel.send('Отказано')

    @commands.command()
    async def help(self, ctx):
        await ctx.send('asdasda')

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