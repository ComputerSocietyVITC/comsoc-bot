import discord
from discord.ext import commands
import json


def read_token():
    with open("data/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)

memFile = open('data/membershipids.txt', 'r')
membershipids = memFile.readlines()


@client.command()
async def membership(ctx, *, id):
    if(str(ctx.channel).startswith("Direct Message")):
        flag = False
        for member in membershipids:
            if member.strip() == id:
                flag = True
                break
        if flag:
            with open("discordmembers.json", "r") as membersJsonFile:
                membersJson = membersJsonFile.read()
                if len(membersJson) == 0:
                    tem = {}
                else:
                    tem = json.loads(membersJson)
                if(tem.get(id)):
                    await ctx.send(f'''Member with IEEE Membership ID {id} already exists.''')
                else:
                    tem[id] = str(ctx.message.author)
                    jsonData = json.dumps(tem, indent=4)
                    f = open("discordmembers.json", "w")
                    f.write(jsonData)
                    f.close()
                    serverid = 870629789667569744
                    server = client.get_guild(serverid)
                    member = server.get_member(ctx.message.author.id)
                    role = discord.utils.get(server.roles, name='member')
                    await member.add_roles(role)
                    await ctx.send("You have been assigned the member role. Go to roles-assignment channel on the discord server to select your Squad and Interests.")
        else:
            await ctx.send("IEEE Membership ID incorrect.")

client.run(token)
