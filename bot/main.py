import discord
import os, random
from os.path import join, dirname
from dotenv import load_dotenv

import bot_commands

client = discord.Client()

DOTENV_PATH = join(dirname(__file__), "keys.env")
load_dotenv(DOTENV_PATH)

TOKEN = os.getenv('BOT_TOKEN')
BOT = bot_commands.spiritBot()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name= 'InterVarsity Newark')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.type) == 'MessageType.new_member':
        return

    if message.content[0] == '!' and message.content[1] == '!':
        response = BOT.command(message.content)
        color = random.randint(0,16777215)
        embed = discord.Embed(
            title = response['title'],
            description = response['text'],
            color = color,
        )
        if(message.author.nick == None):
            embed.set_author(name = message.author.name, icon_url = message.author.avatar_url)
        else:
            embed.set_author(name = message.author.nick, icon_url = message.author.avatar_url)
        
        print(response)
        if response['COM'] == 'bible':
            embed.set_thumbnail(url = "https://img.icons8.com/color/2x/holy-bible.png")
            if 'foot' in response.keys():
                embed.set_footer(text = response['foot'])
        elif response['COM'] == 'joke':
            embed.set_thumbnail(url = "https://img.icons8.com/emoji/2x/zany-face.png")
        elif response['COM'] == 'yoda':
            embed.set_thumbnail(url = "https://img.icons8.com/color/2x/baby-yoda.png")
        elif response['COM'] == 'about':
            embed.set_thumbnail(url = "https://img.icons8.com/color/2x/about.png")
        elif response['COM'] == 'help':
            embed.set_thumbnail(url = "https://img.icons8.com/officel/2x/help.png")
        elif response['title'] == 'Invalid command :(':
            embed.set_thumbnail(url = 'https://img.icons8.com/fluent/2x/cancel.png')
        await message.channel.send(embed = embed)
        await message.delete()

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)