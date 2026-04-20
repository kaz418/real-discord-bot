import discord
import os

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True

client = discord.Client(intents=intents)

EMOJI = "💀"  # 👈 choose the one emoji you want

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    try:
        if reaction.message.author == client.user:
            return

        # add the SAME emoji 12 times
        for _ in range(12):
            await reaction.message.add_reaction(EMOJI)

    except Exception as e:
        print(e)

client.run(os.getenv("TOKEN"))
