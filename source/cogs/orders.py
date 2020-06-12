import discord
from discord.ext import commands

class Orders(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx):
        # await ctx.send("ttetetetete test")
        print(ctx)

def setup(client):
    client.add_cog(Orders(client))