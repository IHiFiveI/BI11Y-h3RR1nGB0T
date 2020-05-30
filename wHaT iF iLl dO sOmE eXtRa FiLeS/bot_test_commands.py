import discord
from discord.ext import commands

def setup(client):
    client.add_cog(bot_commandsCog(client))

class bot_commandsCog():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def hello2(self):
        msg = 'Hello{0.author.mention}'.format(ctx.message)
        await self.send(msg)

