import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = Bot(description="BotBoy is hungry for 1's and 0's", command_prefix="!", pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Created by RJ (Assistant to the Regional Software Engineer)')

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")

@client.command()
async def oliver(*args):
	await client.say(":dog::dog::dog:")



client.run('NDAzNjcxNTA2MTcwOTM3MzQ0.DUKwpw.bBisFKu9QeZDI_4TEO0d2e40jG8')
