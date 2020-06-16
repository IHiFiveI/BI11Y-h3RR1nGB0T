import discord
from discord.ext import commands

from main import prefix

class SimpleMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.goose_expectation = {'ЗАПУСКАЕМ\n░','запускайте гуся', 'гуся!'}
        self.bogdan_expectation = {'░░▄█████','запускайте богдана', 'Богдан!'}
        self.f_expectation = {'f', 'ффф'}
        self.second_h5message = False

    @commands.Cog.listener()
    async def on_ready(self):
        print('initialized bot: {0.user}\n'
              '==============================================\n'.format(self.client))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith(prefix) or message.author == self.client.user:
            return

        if message.author.id == 485330482276466698:
            if self.second_h5message:
                await message.add_reaction('🤚')
            self.second_h5message = not self.second_h5message

        for taken_f in self.f_expectation:
            if message.content.startswith(taken_f) and len(message.content) <= 3:
                await message.channel.send(':regional_indicator_f:')

        for taken_goose in self.goose_expectation:
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
                                            '░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄\n'
                                            '░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄\n'
                                            '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                            '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                            '░░░░░░░░░▄▄▌▌▄▌▌░░░░░\n')

        for taken_bogdan in self.bogdan_expectation:
            if message.content.startswith(taken_bogdan):
                await message.channel.send('░░▄███████▀▀▀▀▀▀███████▄\n'
                                            '░▐████▀▒ЗАПУСКАЕМ▒▀██████▄\n'
                                            '░███▀▒▒▒▒▒ДЯДЮ▒▒▒▒▒▒▀█████\n'
                                            '░▐██▒▒▒▒▒▒БОГДАНА▒▒▒▒▒████▌\n'
                                            '░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌\n'
                                            '░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌\n'
                                            '░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌\n'
                                            '░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌\n'
                                            '░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌\n'
                                            '░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█\n'
                                            '░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀\n'
                                            '░░░░▄██████████████▒▒▐▌\n'
                                            '░░░▀███▀▀████▀█████▀▒▌\n'
                                            '░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐\n'
                                            '░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐\n')

def setup(client):
    client.add_cog(SimpleMessages(client))