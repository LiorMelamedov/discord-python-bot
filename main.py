import discord
from discord.ext import commands
import os
from webserver import keep_alive

client = commands.Bot(command_prefix = '! ')



@client.event
async def on_ready():
    print("Im Ready")

@client.command()
async def say(ctx,*,content):
    await ctx.send(content)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member=None,*,reason=None):
  await ctx.channel.purge(limit=1)
  if not member:
    await ctx.send("Please Mention Somebody To Kick")

  await member.kick(reason=reason)
  await ctx.send(embed=discord.Embed(title=f"{member.name} got kicked by {ctx.author.name}", description=f"Reason: **{reason}**"))
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You Need The `kick members` Permissions To Do That Command")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member:discord.Member=None,*,reason=None):
  await ctx.channel.purge(limit=1)
  if not member:
    await ctx.send("Please Mention Somebody To Ban")

  await member.ban(reason=reason)
  await ctx.send(embed=discord.Embed(title=f"{member.name} got banned by {ctx.author.name}", description=f"Reason: **{reason}**"))
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You Need The `ban members` Permissions To Do That Command")

keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
