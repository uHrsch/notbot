#notbot.py
import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(
        f'Lauf so schnell du kannst {member.name}!'
    )

@bot.command(name='ping', help='Will respond with pong')
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)