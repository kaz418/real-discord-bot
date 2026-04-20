import discord
import os

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

client = discord.Client(intents=intents)

# 👉 Put your 12 reactions here
REACTIONS = [
    "😂", "🔥", "💀", "👏", "❤️", "😎",
    "😮", "😭", "👍", "👎", "🤯", "🎉"
]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    try:
        # Avoid infinite loops (don’t react to bot’s own reactions)
        if reaction.message.author == client.user:
            return

        for emoji in REACTIONS:
            await reaction.message.add_reaction(emoji)

    except Exception as e:
        print(e)

client.run(os.getenv("TOKEN"))
