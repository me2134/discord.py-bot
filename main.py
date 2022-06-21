 #988598060538015815
import discord
import json
from discord.ext import commands

with open('info.json') as f:
    data = json.load(f)
token = data["token"]


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.idle)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency}ms')
@bot.command
async def users(ctx):
  await ctx.send(f'{ctx.guild.name} has {ctx.guild.member_count} users')

bot.run(token)
