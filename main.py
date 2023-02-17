import discord
from discord.ext import commands
import Player
import Items
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

id_items = {
    "FirstItem": 1,
    "SecondItem": 2,
    "Third": 3
}


@client.event
async def on_ready():
    print("ClientBot Ready!")


@client.command()
async def create(ctx):
    user = Player.User(ctx.author)
    user.create(first_name="Miha", last_name="Pidor", nationality="RUS", description="Hello World!")


@client.command()
async def delete(ctx):
    user = Player.User(ctx.author)
    user.delete()


@client.command()
async def add_item(ctx, id: int):
    user = Player.User(ctx.author)
    user.add_item(id)


@client.command()
async def test(ctx):
    user = Player.User(ctx.author)
    print(user.__dict__)

if __name__ == '__main__':
    client.run(config.discord_token)