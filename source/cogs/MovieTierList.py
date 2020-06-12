import json
import discord
from discord.ext import commands

class MovieTierList(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mshow(self, ctx):
