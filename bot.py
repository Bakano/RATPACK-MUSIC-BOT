import os
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

# Get bot token from environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if TOKEN is None:
    print("Error: DISCORD_BOT_TOKEN is not set.")
else:
    bot.run(TOKEN)