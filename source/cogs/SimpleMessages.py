import discord
from discord.ext import commands
import json

from main import prefix
from main import is_permission_granted


class SimpleMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.goose_expectation = {'ЗАПУСКАЕМ\n░', 'запускайте гуся', 'гуся!'}
        self.bogdan_expectation = {'░░▄█████', 'запускайте богдана', 'Богдан!'}
        self.f_expectation = {'f', 'ффф'}
        with open('./json/reaction_list.json', 'r', encoding='utf-8') as f:
            self.emoji_react_list = json.loads(f.read())

    @commands.Cog.listener()
    async def on_ready(self):
        print('initialized bot: {0.user}\n'
              '==============================================\n'.format(self.client))

    async def add_passive_emoji_react(self, message):
        for i in range(len(self.emoji_react_list)):
            if self.emoji_react_list[i]["user_id"] == message.author.id:
                if not self.emoji_react_list[i]["msg_state"]:
                    for j in range(len(self.emoji_react_list[i]["emoji"])):
                        await message.add_reaction(self.emoji_react_list[i]["emoji"][j])
                self.emoji_react_list[i]["msg_state"] = not self.emoji_react_list[i]["msg_state"]

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
