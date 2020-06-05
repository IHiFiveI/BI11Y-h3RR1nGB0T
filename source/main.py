import discord
from discord.ext import commands

f = open('info.txt', 'r')
token = f.read(59)
f.close()
prefix = ","

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("Bot initialized")

client.run(token)