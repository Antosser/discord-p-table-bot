# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv
from ptable import decompose_into_symbols

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content) < 5:
        return

    try:
        decomposition = decompose_into_symbols(message.content)
    except Exception as e:
        print(f"Error decomposing message: {e}")
        return

    if decomposition:
        await message.channel.send(
            "Congratulations! Your message can be written only using symbols from the periodic table! ("
            + ", ".join(["`" + s + "`" for s in decomposition])
            + ")"
        )


client.run(os.getenv("TOKEN"))
