import discord
from discord.ext import commands
from discord.utils import get
import os
import random
from lists import campquote

client = commands.Bot(command_prefix = '|')

@client.event
async def on_ready():
  print("Bot is ready.")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if str(message.channel) == 're-education-camp':
    await message.channel.send(random.choice(campquote(message.author)))

  await client.process_commands(message)

def findhighestrole(ctx, member): #Function to find highestrole
  highestrole = ''
  for roles in ctx.guild.roles:
    for roles2 in member.roles:
      if roles2 == roles:
        highestrole = roles2
  return highestrole

@client.command(pass_context=True)
async def imprison(ctx, member : discord.Member): #Imprison command
  authorhighestrole = findhighestrole(ctx, ctx.author)
  memberhighestrole = findhighestrole(ctx, member)

  if str(ctx.author) == 'manspider011#6289':
    await ctx.channel.send('idiot manspider')
    return

  if (authorhighestrole > memberhighestrole) or (authorhighestrole == memberhighestrole and str(ctx.author) == 'manspider011#6289'):
    roles = [get(ctx.guild.roles, name='member'), get(ctx.guild.roles, name='.'), get(ctx.guild.roles, name='stuy')]
    
    for role in roles:
      await member.remove_roles(role)
    await member.add_roles(get(ctx.guild.roles, name='p'))
    await ctx.channel.send(f'@{member} has been imprisoned.')

  else:
    await ctx.channel.send(f'Your permissions are not high enough to imprison @{member}.')

@client.command(pass_context=True)
async def free(ctx, member : discord.Member): #Free command
  authorhighestrole = findhighestrole(ctx, ctx.author)
  memberhighestrole = findhighestrole(ctx, member)

  if str(ctx.author) == 'manspider011#6289':
    await ctx.channel.send('idiot manspider')
    return

  if (authorhighestrole > memberhighestrole) or (authorhighestrole == memberhighestrole and str(ctx.author) == 'manspider011#6289'):

    roles = [get(ctx.guild.roles, name='member'), get(ctx.guild.roles, name='.'), get(ctx.guild.roles, name='stuy')]

    for role in roles:
      await member.add_roles(role)
    await member.remove_roles(get(ctx.guild.roles, name='p'))
    await ctx.channel.send(f'@{member} has been freed.')

  else:
    await ctx.channel.send(f'Your permissions are not high enough to free @{member}.')


client.run(os.environ['TOKEN'])