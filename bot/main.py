import discord, asyncio
import os, random
from os.path import join, dirname
from discord.errors import NotFound
from dotenv import load_dotenv
from discord.utils import get

import bot_commands, embeds

intents = discord.Intents().all()
client = discord.Client(prefix = '', intents=intents)

DOTENV_PATH = join(dirname(__file__), "keys.env")
load_dotenv(DOTENV_PATH)

TOKEN = os.getenv('BOT_TOKEN')
BOT = bot_commands.spiritBot()

def choose_embed(embed):
    if embed.lower() == 'dm':
        return embeds.DM
    elif embed.lower() == 'welcome':
        return embeds.WELCOME
    elif embed.lower() == 'nickname':
        return embeds.NICKNAME
    elif embed.lower() == 'roles':
        return embeds.ROLES
    elif embed.lower() == 'discord':
        return embeds.DISCORD
    elif embed.lower() == 'thanks':
        return embeds.THANKS
    return embeds.ERR_404

@client.event
async def on_ready():
    rand_status = random.randint(0, 4)
    if rand_status == 0:
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = 'the Word of God'))
    elif rand_status == 1:
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = 'Worship Music'))
    elif rand_status == 2:
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = 'a sermon'))
    elif rand_status == 3:
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = 'The Passion of the Christ'))
    print("I am online")

@client.event
async def on_member_join(member):
    embedded_dm = embeds.DM
    await member.create_dm()
    async for message in member.history(limit = 15):
        if message.author.id == client.user.id:
            await message.delete()
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
    
    elif message.content[0] == '.' and msg[0][1:].lower() == 'update':
        if len(msg) != 3:
            await message.channel.send(embed = embeds.INC_PARAMS, delete_after = 30)
        else:
            msgID = int(msg[1])
            try:
                msg_edit = await message.channel.fetch_message(msgID)
                embed = choose_embed(msg[2])
                if embed == embeds.ERR_404:
                    await message.channel.send(embed = embeds.ERR_404, delete_after = 30)
                else:
                    await msg_edit.edit(embed = embed)
            except NotFound:
                await message.channel.send(embed = embeds.DNE, delete_after = 30)
        await message.delete()
    
    elif message.content[0] == '.' and message.content[1] == '$':
        if message.content[2:].lower() == 'welcome':
            await message.channel.send(embed = embeds.WELCOME)
        elif message.content[2:].lower() == 'nickname':
            await message.channel.send(embed = embeds.NICKNAME)
        elif message.content[2:].lower() == 'roles':
            await message.channel.send(embed = embeds.ROLES)
        elif message.content[2:].lower() == 'discord':
            await message.channel.send(embed = embeds.DISCORD)
        elif message.content[2:].lower() == 'thanks':
            await message.channel.send(embed = embeds.THANKS)
        await message.delete()

client.run(TOKEN)