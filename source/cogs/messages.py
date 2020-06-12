import discord
from discord.ext import commands

class MessageMe(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.goose_expectation = {'ЗАПУСКАЕМ\n░','запускайте гуся', 'гуся!'}
        self.f_expectation = {'f', 'ффф'}

    @commands.Cog.listener()
    async def on_ready(self):
        print('initialized bot: {0.user}\n'
              '==============================================\n'.format(self.client))

    @commands.Cog.listener()
    async def on_message(self, message):
        # do someting with prefix
        if message.content.startswith(',') or message.author == self.client.user:
            return

        for taken_f in self.f_expectation:
            if message.content.endswith(taken_f) and message.content.startswith(taken_f):
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
                                           '░░░▐░░░░▐▒▒▒▒▒▒▒▒▒▒▒▀▄\n'
                                           '░░░▐░░░░▀▄▒▒▒▒▒▒▒▒▒▒▒▄\n'
                                           '░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▀▄\n'
                                           '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                           '░░░░░░░░░░░▌▌░▌▌░░░░░\n'
                                           '░░░░░░░░░▄▄▌▌▄▌▌░░░░░\n')

def setup(client):
    client.add_cog(MessageMe(client))