import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

if __name__ == '__main__':
    client.run(config.discord_token)