import discord

LIST_OF_BAD_WORDS = [
    "heck",
    "dumb",
    "stupid",
    "meanie",
    "stinky",
    "smelly",
    "freak",
    "freaking",
    "frik",
    "friggin",
    "jerk",
    "nincompoop",
    "silly billy",
    "gg",
    "yipppeeee",
    "nice shot",
    "fortnite",
    "suck",
    "sucks"
]

def run_discord_bot():
    TOKEN = 'MTIwMDIyMjUyMzM5NzI1MTA3Mg.GemtGS.40zplvTFAwvZgidG_Fg5ZF4JjI10GI60qHM2OU'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now guarding your server from badmen.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        user_message = str(message.content)
        user_message = user_message.split(" ")

        print(f'{message.author} said {user_message} in {message.channel}')

        for word in user_message:
            if word in LIST_OF_BAD_WORDS:
                await message.delete()
                await message.channel.send("You can't say bad things here!")
                break
        

    client.run(TOKEN)