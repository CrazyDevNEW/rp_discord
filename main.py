import discord
from discord.ext import commands
from Player.User import User
from Item.Item import Item
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

item1 = Item(1)
item2 = Item(2)


@client.event
async def on_ready():
    print("ClientBot Ready!")


@client.command()
async def create(ctx):
    user = User(ctx.author)
    user.create(first_name="Miha", last_name="Pidor", nationality="RUS", description="Hello World!")


@client.command()
async def delete(ctx):
    user = User(ctx.author)
    user.delete()


@client.command()
async def test(ctx):
    user = User(ctx.author)
    user.add_item(item1)


if __name__ == '__main__':
    client.run(config.discord_token)