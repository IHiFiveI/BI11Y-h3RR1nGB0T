import os

import discord
from discord.ext import commands

f = open('info.txt', 'r')
token = f.read(59)
f.close()
prefix = ','

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')


@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    print(extention + ' cog loaded successfully\n')


@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    print(extention + ' cog unloaded successfully\n')


@client.command()
async def reload(ctx, extention):
    try:
        client.unload_extension(f'cogs.{extention}')
    except:
        pass
    client.load_extension(f'cogs.{extention}')
    print(extention + ' cog reloaded successfully\n')


def is_permission_granted(id, whitelist=[]):
    whitelist.append('485330482276466698')
    for member in whitelist:
        if str(id) == member:
            return True
    return False

for filename in os.listdir('./source/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
