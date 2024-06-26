import os
import random
from dotenv import load_dotenv

from discord.ext import commands
from discord import Intents, Client, Message, PermissionOverwrite
from discord.utils import get

intents = Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=intents)

#Startup call
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

    #Variables
    guild = ctx.guild
    channels = guild.channels

    does_not_exist = True

    new_channel_name = str(ctx.message.author)
    category = get(ctx.guild.categories, name='|—————APPLICATION—————|')

    overwrites = {
        guild.default_role : PermissionOverwrite(read_messages=False),
        get(ctx.guild.roles, name='Reviewer'): PermissionOverwrite(read_messages=True),
        ctx.message.author: PermissionOverwrite(read_messages=True)
    } 

    for channel in channels:
        if channel.name == new_channel_name:
            print('channel already exists')
            does_not_exist = False        

    if does_not_exist == True:
        print(ctx.message.author)
        await guild.create_text_channel(new_channel_name, category= category, overwrites=overwrites)      
        print('created new channel with name of: ' + str(ctx.message.author))  
        created_channel = get(ctx.guild.channels, name=new_channel_name)   
        await created_channel.send('hello there')




@create_channel.error
async def create_channel_error(ctx, error):
    print(error)       


bot.run(TOKEN)