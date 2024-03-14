import os
import discord
from discord import app_commands
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') # Set token in .env file
    YOUR_ID = "Insert your discord ID here"
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running.")
        try:
            await tree.sync()
            print("Commands synced successfully.")
        except Exception as e:
            print(e)

    @tree.command(name="hello")
    async def hello(interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!")

    @tree.command(name="speak")
    @app_commands.describe(thing_to_say = "What should I say?")
    async def speak(interaction, thing_to_say: str):
        await interaction.response.send_message(f"{interaction.user.name} said: {thing_to_say}")

    @tree.command(name='sync', description='Owner only')
    async def sync(interaction: discord.Interaction):
        if interaction.user.id == YOUR_ID:
            await tree.sync()
            print('Command tree synced.')
        else:
            await interaction.response.send_message('You must be the owner to use this command!')

    client.run(DISCORD_TOKEN)