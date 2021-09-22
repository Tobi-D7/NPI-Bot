import discord
from discord.ext import commands
import datetime

import os

TK = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='>', description="NPI-Bot ©2021")

@bot.command()
async def sumf(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne + numTwo)

@bot.command()
async def diff(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne - numTwo)

@bot.command()
async def prof(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne * numTwo)

@bot.command()
async def quof(ctx, numOne: float, numTwo: float):
    await ctx.send(numOne / numTwo)

@bot.command()
async def sumi(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def difi(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne - numTwo)

@bot.command()
async def proi(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne * numTwo)

@bot.command()
async def quoi(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne / numTwo)



@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Npi-dev", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value="TobiD7#9836")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.add_field(name="Ping", value=f"{bot.latency}")
     #embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)
@bot.command()
async def helps(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Help Commandlist", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Display Server Info", value=">info")
  
    await ctx.send(embed=embed)


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=">helps"))
    print('+----------+\n|  NPI-Bot |\n|  © 2021  |\n+----------+\nBot Init success!')
    channel = bot.get_channel(889596748903882812)
    await channel.send('''''+----------+\n|  NPI-Bot |\n|  © 2021 |\n+----------+\nBot Init success!''')

@bot.listen()
async def on_message(message):
  if message.author == bot.user or message.author.bot:
   return
   await bot.process_commands(message)
  
   
   
  embed = discord.Embed(title=f"{message.guild.name}", description="Message-Log", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
  embed.add_field(name="Author", value=f"{message.author}")
  embed.add_field(name="Channel", value=f"{message.channel}")
  embed.add_field(name="Text", value=f"{message.content}")
  
  channel = bot.get_channel(889601437305282623)

  await channel.send(embed=embed)
bot.run(TK)
