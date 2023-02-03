import discord
from discord.ext import commands
from Player import User
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
test = User.User()

if __name__ == '__main__':
    client.run(config.discord_token)
