import discord
from badwords import LIST_OF_BAD_WORDS

def run_discord_bot():
    TOKEN = "MTIwMTE2OTE4MzUxODQ5ODkxNg.GQ7PDt.4G7ighZXfjAZip-9fxTMgh8CDPxeomKk7dN8AY"
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now purifying the Christian Minecraft server!")

    @client.event
    async def on_message(message):
        
    
    client.run(TOKEN)