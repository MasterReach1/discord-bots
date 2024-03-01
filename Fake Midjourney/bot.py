import os
from openai import OpenAI
import discord
import urllib.request
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') # Set token in .env file
    intents = discord.Intents.default()
    intents.message_content = True
    aiClient = OpenAI()
    discordClient = discord.Client(intents=intents)

    @discordClient.event
    async def on_ready():
        print(f"{discordClient.user} is now running.")

    @discordClient.event
    async def on_message(message):
        if message.content.startswith("?generate"):
            prompt = message.content.replace('?generate', '')
            print(prompt)

            await message.delete()
            await message.channel.send("Generating image, please wait...")
            
            response = aiClient.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            urllib.request.urlretrieve(image_url, "generated_image.png")

            await message.channel.send(content=f"Image for: {prompt}", file=discord.File('generated_image.png'))

    discordClient.run(DISCORD_TOKEN)