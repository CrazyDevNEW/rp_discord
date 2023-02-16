import discord
from discord.ext import commands
from Player.User import User
from Items.Item import Item
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
    user = User(ctx.author)
    user.create(first_name="Miha", last_name="Pidor", nationality="RUS", description="Hello World!")


@client.command()
async def delete(ctx):
    user = User(ctx.author)
    user.delete()


@client.command()
async def test(ctx):
    user = User(ctx.author)
    items = user.get_items(id_items.get("Third"))
    for i in items:
        print(i)

if __name__ == '__main__':
    client.run(config.discord_token)