import discord
from discord.ext import commands
from antispam import AntiSpamHandler

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=data["prefix"], intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.handler = AntiSpamHandler(client, warn_threshold=5, kick_threshold=8,message_interval=1000,guild_warn_message="Stop spamming! wait 15 and then you can send a message without getting kicked.")





@client.event
async def on_message(message):
    await client.handler.propagate(message)
    await client.process_commands(message)
