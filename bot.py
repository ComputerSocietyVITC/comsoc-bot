from os import read
import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


@client.event
async def on_message(message):
    if str(message.channel).startswith("Direct Message"):
        if message.content.find("$membership") == 0:
            print(message.author)
            print(message.content)
            await message.channel.send("Please wait while we validate your Membership ID")

client.run(token)
