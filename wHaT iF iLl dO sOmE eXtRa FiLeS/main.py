import discord
from discord.ext import commands

import bot_test_commands

token = "NzE1NDQ1ODc4Mzk1MjQwNDcw.Xs9VOA.XRUUl4GBZ4Wr74KE3KpD_wa30Wc"
prefix = ","
startup_extensions = ["bot_test_commands"]

bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)