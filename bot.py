import os
import random
from dotenv import load_dotenv

from discord.ext import commands
from discord import Intents, Client, Message

intents = Intents.default()
intents.message_content = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord successfully')

async def is_chnanel(ctx):
    return ctx.channel.id == 1233138130173952122    

@bot.command(name='alive?', help='command to check if the bot is alive')
async def test_alive(ctx):
    await ctx.send('Its testing at least')

@bot.command(name='submit')

@commands.check(is_chnanel)
async def create_channel(ctx):
    new_channel_name = str(ctx.message.author)
    guild = ctx.guild
    channels = guild.channels
    does_not_exist = True
    for channel in channels:
        if channel.name == new_channel_name:
            does_not_exist = False
            

    if does_not_exist == True:
        await guild.create_text_channel(new_channel_name)      
        print('created new channel with name of: ' + str(ctx.message.author))  

@create_channel.error
async def create_channel_error(ctx, error):
    print(error)        

bot.run(TOKEN)