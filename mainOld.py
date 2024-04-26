

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import send_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Set up the bots
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def recieve_message(message, user_message):
    if not user_message:
        print('Message waas empty')
        return

    try:
        response = send_message(user_message)
        await message.channel.send(response) 
    except Exception as e:
        print(e)

#Handle startup
@client.event
async def on_ready():
    print(f'{client.user} is now running')

#Handle incoming messages
async def on_message(message):
    if message.author == client.user:
        return

    username = message.author
    user_message = message.content
    channel = message.channel

    print(f'[{channel}] {username}: "{user_message}"')    
    await send_message(message, user_message)

    def main():
        client.run(token=TOKEN)

    main()