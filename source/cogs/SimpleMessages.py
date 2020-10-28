import discord
from discord.ext import commands
import json
import os
import random

from main import prefix
from main import is_permission_granted


class SimpleMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.goose_expectation = {'ЗАПУСКАЕМ\n░', 'запускайте гуся', 'гуся!'}
        self.bogdan_expectation = {'░░▄█████', 'запускайте богдана', 'Богдан!'}
        self.f_expectation = {'f', 'ффф'}
        self.servers_own_reactions = ""

    def get_reaction(self, arg):
        self.server_reaction_path = './json/{}'.format(arg)

        if not os.path.exists(self.server_reaction_path):
            os.mkdir(self.server_reaction_path)
            with open(self.server_reaction_path + '/reaction_list.json', 'w') as fp:
                fp.write('[\n]')

        with open(self.server_reaction_path + '/reaction_list.json', 'r', encoding='utf-8') as f:
            self.emoji_react_list = json.loads(f.read())
        
        return self.emoji_react_list

    @commands.Cog.listener()
    async def on_ready(self):
        print('initialized bot: {0.user}\n'
              '==============================================\n'.format(self.client))

    async def add_passive_emoji_react(self, message):
        self.servers_own_reactions = self.get_reaction(message.guild.id)
        for i in range(len(self.servers_own_reactions)):
            if self.servers_own_reactions[i]["user_id"] == message.author.id:
                if random.randint(1,9) % 3 == 0:
                    for j in range(len(self.servers_own_reactions[i]["emoji"])):
                        await message.add_reaction(self.servers_own_reactions[i]["emoji"][j])

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith(prefix) or message.author == self.client.user:
            return

        await self.add_passive_emoji_react(message)

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
