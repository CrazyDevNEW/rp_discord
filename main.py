import discord
from discord.ext import commands
from sqlalchemy import Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.mysql import BIGINT, MEDIUMINT, TINYINT, DATETIME, JSON, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import config

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


class UserDB(declarative_base()):
    # __tablename__ = "users"
    # id = Column(MEDIUMINT, primery_key=True, autoincrement=True)
    # discord_id = Column(BIGINT, unique=True, nullable=False)
    # first_name = Column(VARCHAR(50), unique=False, nullable=False)
    # last_name = Column(VARCHAR(50), unique=False, nullable=False)
    # nationality = Column(VARCHAR(92), unique=False, nullable=False)
    # skin = Column(JSON, unique=False, nullable=False)
    pass

a = UserDB()
print(a.__dict__)

@client.event
async def on_ready():
    pass


if __name__ == '__main__':
    client.run(config.discord_token)
    engine = create_engine(config.dbUrl)
    DBSession = sessionmaker(binds={declarative_base(): engine}, expire_on_commit=False)
    session = DBSession()
    declarative_base().metadata.create_all(engine)
