import os
import discord
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') # Set token in .env file
    intents = discord.Intents.default()
    intents.message_content = True
    discordClient = discord.Client(intents=intents)

    @discordClient.event
    async def on_ready():
        print(f"{discordClient.user} is now running.")

    @discordClient.event
    async def on_message(message):
        pass # insert bot on_message() code here

    discordClient.run(DISCORD_TOKEN)