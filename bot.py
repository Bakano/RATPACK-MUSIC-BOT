import discord
from discord.ext import commands

# Define command prefix
PREFIX = '!'

# Create bot instance with prefix
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Example command: Play music
@bot.command()
async def play(ctx, *, url: str):
    await ctx.send(f'Playing music from {url}')

# Example command: Stop music
@bot.command()
async def stop(ctx):
    await ctx.send('Stopping music')

# Run bot
TOKEN = 'MTM0ODM1MjQzMTM0NzQ2NjM3MQ.GB4S-l.yNkclw_d6PF8_4a5ohzOHFO_c3bk-F0CAD4oyY'
bot.run(TOKEN)