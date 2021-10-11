import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '|')

@client.event
async def on_ready():
  print("Bot is ready.")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("|eee"):
    mentioned = message.mentions
    await message.channel.send(mentioned)

  if message.content.startswith('|name'):
    await message.channel.send(message.author.name)

  await client.process_commands(message)

@client.command()
async def imprison(ctx, member : discord.Member, hour):
  await ctx.channel.send(f'@{member} has been imprisoned for {hour}.')


client.run(os.environ['TOKEN'])