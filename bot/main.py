import discord
import os, random
from os.path import join, dirname
from dotenv import load_dotenv
from discord.utils import get

import bot_commands, embeds

intents = discord.Intents().all()
client = discord.Client(prefix = '', intents=intents)

DOTENV_PATH = join(dirname(__file__), "keys.env")
load_dotenv(DOTENV_PATH)

TOKEN = os.getenv('BOT_TOKEN')
BOT = bot_commands.spiritBot()

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = 'the Word of God'))
    print("I am online")

@client.event
async def on_member_join(member):
    embedded_dm = embeds.DM_EMBED
    await member.create_dm()
    await member.dm_channel.send(embed = embedded_dm)
    if(member.nick == None):
        await member.edit(nick = 'First Last 📛')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.type) == 'MessageType.new_member':
        return
    msg = message.content.split()
    print(msg)
    if message.content[0] == '$':
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

    elif message.content[0] == '.' and msg[0][1:].lower() == 'embed':
        text = ''
        if(msg[2].startswith('\"') and msg[-2][-1]):
            for word in msg[2:-1]:
                text += (word + ' ')
        embed = discord.Embed(
            title = msg[1],
            description = text[1:-2],
            color = int(msg[-1], 16))
        embed.set_author(name = message.author.nick, icon_url = message.author.avatar_url)
        embed.set_thumbnail(url = message.author.avatar_url)
        await message.channel.send(embed = embed)
        await message.delete()       
    
    elif message.content[0] == '.' and message.content[1] == '$':
        if message.content[2:].lower() == 'welcome':
            await message.channel.send(embed = embeds.WELCOME)
            await message.delete()
        elif message.content[2:].lower() == 'nickname':
            await message.channel.send(embed = embeds.NICKNAME)
            await message.delete()
        elif message.content[2:].lower() == 'roles':
            await message.channel.send(embed = embeds.ROLES)
            await message.delete()
        elif message.content[2:].lower() == 'discord':
            await message.channel.send(embed = embeds.DISCORD)
            await message.delete()
        elif message.content[2:].lower() == 'thanks':
            await message.channel.send(embed = embeds.THANKS)
            await message.delete()

client.run(TOKEN)