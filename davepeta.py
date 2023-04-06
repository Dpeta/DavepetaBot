#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import random

import discord

import commands
from reacts import reacts, user_1

activity = discord.Activity(name="dp!help", details="dp!help", type=discord.ActivityType.playing)
intents = discord.Intents.none()
intents.message_content = True
intents.guild_messages = True
intents.dm_messages = True

class Davepeta(discord.Client):
    async def on_connect(self):
        print('Connecting! <3')
        if not hasattr(self, 'dpeta_responding'):
            self.dpeta_responding = []
        if not hasattr(self, 'help_embed'):
            # Command help
            desc = '__**Commands:**__'
            for command in dir(commands):
                if not command.startswith('__'):
                    desc += '\n**- %s**' % command
            desc += '\n\n'
            
            # Reacts help:
            desc += '__**Reacts:**__'
            for user in reacts:
                desc += '\n**- <@%s>**: ' % user
                for emote in reacts[user]:
                    desc += ' ' + emote
            desc += '\n\n'
                    
            # Unique reacts help (manual)
            desc += '__**Unique reacts:**__'
            desc += '\n**- <@%s>**: %s (10%% chance)' % (user_1,
                                                         '<:peep_candy:1003094461561180220>')
            desc += '\n\n'

            # Unique responses help (manual)
            desc += ('__**Unique responses:**__'
                     '\n**- Aradia**'
                     '\n**- CH quirk**')

            self.help_embed = discord.Embed(title="Davepeta Bot Help",
                          description=desc)

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.author.id in reacts.keys():
            for user in reacts:
                if message.author.id == user:
                    for emote in reacts[user]:
                        await message.add_reaction(emote)

        message_folded = message.content.casefold()

        # Special reacts
        if message.author.id == user_1:
            if not random.getrandbits(4):
                await message.add_reaction('<:peep_candy:1003094461561180220>')
                
        if "aradia" in message_folded:
            await message.add_reaction('<:aradiaflushed:782055771537276939>')

        if "eridan" in message_folded or "listen_up_all_you_landwwellers" in message_folded:
            await message.add_reaction('<:listen_up_all_you_landwwellers:1003291164184678501>')

        # Responses
        if "‖ː‖" in message_folded:
            await message.channel.send('D:')

        # Commands
        if message.content.startswith('dp!'):
            msg = message.content[3:]
            command = msg.split(' ')[0]
            try:
                if command.startswith('__'):
                    raise AttributeError
                cmd = getattr(commands, command)
                await cmd(self, message)
                return
            except AttributeError:
                if random.getrandbits(3):
                    await message.channel.send("That's not a command!")
                else:
                    await message.channel.send("That's not a command?")
            except Exception as e:
                print(e)

        # Repeater
        if message.author.id in self.dpeta_responding:
            await message.channel.send(message.content)

dpeta = Davepeta(intents=intents,
                 activity=activity,
                 allowed_mentions=discord.AllowedMentions.none(),
                 member_cache_flags=discord.MemberCacheFlags.none(),
                 max_messages=None)
dpeta.run(os.environ["DAVEPETA_TOKEN"])
    
