import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix = '|')

@client.event
async def on_ready():
  print("Bot is ready.")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('|name'):
    await message.channel.send(message.author.name)

  await client.process_commands(message)

def findhighestrole(ctx, member):
  highestrole = ''
  for roles in ctx.guild.roles:
    for roles2 in member.roles:
      if roles2 == roles:
        highestrole = roles2
  return highestrole

@client.command(pass_context=True)
async def imprison(ctx, member : discord.Member):
  if str(ctx.author) == 'manspider011#6289':
    await ctx.channel.send('idiot manspider')
    return

  if findhighestrole(ctx, ctx.author) > findhighestrole(ctx, member):
    memberrole = get(ctx.guild.roles, name='member')
    role = get(ctx.guild.roles, name='.')
    stuy = get(ctx.guild.roles, name='stuy')
    await member.remove_roles(memberrole)
    await member.remove_roles(role)
    await member.remove_roles(stuy)
    await ctx.channel.send(f'@{member} has been imprisoned.')
  else:
    await ctx.channel.send(f'Your permissions are not high enough to imprison @{member}.')

@client.command(pass_context=True)
async def free(ctx, member : discord.Member):
  if str(ctx.author) == 'manspider011#6289':
    await ctx.channel.send('idiot manspider')
    return

  if findhighestrole(ctx, ctx.author) > findhighestrole(ctx, member):
    memberrole = get(ctx.guild.roles, name='member')
    role = get(ctx.guild.roles, name='.')
    stuy = get(ctx.guild.roles, name='stuy')
    await member.add_roles(memberrole)
    await member.add_roles(role)
    await member.add_roles(stuy)
    await ctx.channel.send(f'@{member} has been freed.')
  else:
    await ctx.channel.send(f'Your permissions are not high enough to free @{member}.')


client.run(os.environ['TOKEN'])