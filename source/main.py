import discord
from discord.ext import commands

f = open('info.txt', 'r')
token = f.read(59)
f.close()
prefix = ","

# client = commands.Bot(command_prefix = prefix)
client = discord.Client()

@client.event
async def on_ready():
    print("Initialized bot: {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        return

    if message.author == client.user:
        return

    goose_expectation = {'ЗАПУСКАЕМ\n░','g'}

    for taken_goose in goose_expectation:
        if message.content.startswith(taken_goose):
            await message.channel.send('ЗАПУСКАЕМ\n'
                                       '░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░\n'
                                       '▄███▀░◐░░░▌░░░░░░░\n'
                                       '░░░░▌░░░░░▐░░░░░░░\n'
                                       '░░░░▐░░░░░▐░░░░░░░\n'
                                       '░░░░▌░░░░░▐▄▄░░░░░\n'
                                       '░░░░▌░░░░▄▀▒▒▀▀▀▀▄\n'
                                       '░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄\n'
                                       '░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄\n'
                                       '░░░▐░░░░▀▄▒▒▒▒▒▒▒▒▒▒▒▄\n'
                                       '░░░░▀▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄\n'
                                       '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                       '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                       '░░░░░░░░░▄▄▌▌▄▌▌░░░░░\n')

client.run(token)