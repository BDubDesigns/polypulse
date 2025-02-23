# polypulse/main.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from discord.ext import commands
from discord import app_commands
import config

# Set up intents (default + any extras you need)
intents = discord.Intents.default()
intents.message_content = True  # Optional, only if you use message content elsewhere

# Initialize the bot (prefix is optional for slash-only bots)
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    try:
        # Sync the command tree to register slash commands
        synced = await bot.tree.sync()
        await bot.tree.sync(guild=discord.Object(id=1340103678799122594))
        print(f"Synced {len(synced)} command(s): {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Define a slash command
@bot.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# Run the bot
if __name__ == "__main__":
    bot.run(config.DISCORD_TOKEN)