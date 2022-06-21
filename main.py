import discord
import json
from discord.ext import commands

with open('info.json') as f: # Going into the json file with the toke, and setting the variable "token" to the bots token
    data = json.load(f)
token = data["token"]


intents = discord.Intents.all() # Enable all intents
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.idle, activity =discord.Game("game"))

@bot.command()
async def ping(ctx): # Finds the latency of the bot
    await ctx.send(f'{bot.latency}ms')
    
@bot.command()
async def users(ctx): # Finds the number of users in the guild
  await ctx.send(f'{ctx.guild.name} has {ctx.guild.member_count} users')

bot.run(token)