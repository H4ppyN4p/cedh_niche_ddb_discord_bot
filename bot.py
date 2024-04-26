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

@bot.command(name='alive?', help='command to check if the bot is alive')
async def test_alive(ctx):
    await ctx.send('Its testing at least')

bot.run(TOKEN)