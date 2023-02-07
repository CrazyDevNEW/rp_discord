import discord
from discord.ext import commands
from Player.User import User
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ClientBot Ready!")


@client.command()
async def test(ctx):
    user = User(ctx.author)
    print(user.id)

if __name__ == '__main__':
    client.run(config.discord_token)