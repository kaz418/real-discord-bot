import discord
import os
import asyncio

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True
intents.guilds = True

EMOJIS = ["😂", "🔥", "💀"]

def create_bot(name):
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{name} online as {client.user}")

    @client.event
    async def on_reaction_add(reaction, user):
        if user.bot:
            return

        try:
            if reaction.message.author == client.user:
                return

            for emoji in EMOJIS:
                await reaction.message.add_reaction(emoji)

        except Exception as e:
            print(f"{name} error:", e)

    return client


async def run_bot(name, token):
    try:
        client = create_bot(name)
        await client.start(token)
    except Exception as e:
        print(f"{name} failed to start:", e)


async def main():
    tokens = [
        os.getenv("TOKEN_1"),
        os.getenv("TOKEN_2"),
        os.getenv("TOKEN_3"),
        os.getenv("TOKEN_4"),
        os.getenv("TOKEN_5"),
        os.getenv("TOKEN_6"),
        os.getenv("TOKEN_7"),
        os.getenv("TOKEN_8"),
        os.getenv("TOKEN_9"),
        os.getenv("TOKEN_10"),
        os.getenv("TOKEN_11"),
        os.getenv("TOKEN_12"),
    ]

    tasks = []

    for i, token in enumerate(tokens, start=1):
        if token:  # prevents crash if missing
            tasks.append(run_bot(f"Bot{i}", token))
        else:
            print(f"Bot{i} missing token!")

    await asyncio.gather(*tasks)


asyncio.run(main())
