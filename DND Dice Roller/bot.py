import os
import discord
from dotenv import load_dotenv
from random import Random as r
from discord.ext import commands

def run_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.command(name="roll")
    async def roll(ctx, dice_type: int, amount_of_dice:int = 1):
        dice = []
        
        for i in range(amount_of_dice):
            dice.append(r.randint(1, dice_type))

        message = f"Results of {amount_of_dice} d{dice_type} rolled:"

        for i in range(len(dice)):
            message += f"\n {i}. {dice[i]}"

        await ctx.send(message)