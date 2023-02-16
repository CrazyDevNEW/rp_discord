import discord
from discord.ext import commands
from Player.User import User
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ClientBot Ready!")


@client.command()
async def create(ctx):
    user = User(ctx.author)
    user.create(first_name="Oleg", last_name="Rahmatullin", nationality="RUS", description="Hello World!")


@client.command()
async def delete(ctx):
    user = User(ctx.author)
    user.delete()


@client.command()
async def test(ctx):
    user = User(ctx.author)
    user.real_currency = 10


if __name__ == '__main__':
    client.run(config.discord_token)