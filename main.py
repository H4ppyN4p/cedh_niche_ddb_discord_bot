import os

import discord
from discord import Intents, Client, Message
from dotenv import load_dotenv

load_dotenv
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'It lives?':
        await message.channel.send('Its certainly testing')


#class CustomClient(discord.Client):
    #async def on_ready(self):
        #print(f'{self.user} has connected to Discord')

#client = CustomClient(intents=intents)

client.run(TOKEN)    