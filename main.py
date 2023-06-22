import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)
auth_token = os.getenv('TOKEN')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(auth_token)