import discord
import os
from dotenv import load_dotenv
from badwords import LIST_OF_BAD_WORDS

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('discord_token')
    print(TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now purifying the Christian Minecraft server!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        user_message = str(message.content)
        user_message = user_message.split(" ")

        for word in user_message:
            if word in LIST_OF_BAD_WORDS:
                await message.delete()
                await message.channel.send(f"You can't say {word} here!")
                break
    
    client.run(TOKEN)