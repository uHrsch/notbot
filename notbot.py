import discord
from discord.ext import commands
from discord.ext.tasks import loop
from twitch import *

with open("./config.json") as config_file:
    config = json.load(config_file)

discord_token = config["discord_token"]

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


@loop(seconds=90)
async def check_twitch_online_streamers():
    channel = bot.get_channel(901486647366025249)
    if not channel:
        return
    
    notifications = get_notifications

    for notification in notifications:
        await channel.send("streamer {} ist jetzt online: {}".format(notification["user_login"], notification))



check_twitch_online_streamers.start()
bot.run(discord_token)