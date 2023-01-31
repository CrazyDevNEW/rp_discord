import discord
from discord.ext import commands
from sqlalchemy import Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.mysql import BIGINT, MEDIUMINT, TINYINT, DATETIME, JSON, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
import config


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
Model = declarative_base()


class UserDB(Model):
    __tablename__ = 'users'
    id = Column(MEDIUMINT, primary_key=True, autoincrement=True)
    discordId = Column(BIGINT, unique=True, nullable=False)
    firstName = Column(VARCHAR(50), unique=False, nullable=False)
    lastName = Column(VARCHAR(50), unique=False, nullable=False)
    money = Column(BIGINT, unique=False, nullable=False, default=0)
    nationality = Column(VARCHAR(50), unique=False, nullable=False, default="US")
    exp = Column(MEDIUMINT, unique=False, nukkable=False, default=0)
    sex = Column(VARCHAR(30), unique=False, nullable=False)
    description = Column(VARCHAR(180), unique=False, nullable=True)
    skin = Column(JSON, unique=False, nullable=False)
    createAt = Column(DATETIME, unique=False, nullable=False)
    latestInGame = Column(DATETIME, unique=False, nullable=True)


class InGameDB(Model):
    __tablename__ = 'ingames'
    id = Column(MEDIUMINT, primary_key=True, autoincrement=True)
    userId = Column(ForeignKey('users.id'), unique=True, nullable=False)
    user = relationship('UserDB')
    hp = Column(TINYINT, nullable=False, default=100)
    arm = Column(TINYINT, nullable=False, default=0)
    effects = Column(JSON, unique=False, nullable=False)
    inHands = Column(BIGINT, nullable=False)
    position = Column(JSON, unique=False, nullable=False)
    joinAt = Column(DATETIME, unique=False, nullable=False)


class ItemDB(Model):
    __tablename__ = 'items'
    id = Column(MEDIUMINT, primary_key=True, autoincrement=True)
    itemId = Column(BIGINT, unique=True, nullable=False)
    itemType = Column(VARCHAR(30), unique=False, nullable=False)
    name = Column(VARCHAR(30), unique=False, nullable=False)
    description = Column(VARCHAR(30), unique=False, nullable=False)
    price = Column(BIGINT, unique=False, nullable=False)
    createAt = Column(DATETIME, unique=False, nullable=False)


class InvetoryDB(Model):
    __tablename__ = 'inventories'
    id = Column(MEDIUMINT, primary_key=True, autoincrement=True)
    userId = Column(ForeignKey('users.id'), unique=False, nullable=False)
    user = relationship('UserDB')
    itemId = Column(ForeignKey('items.id'), unique=False, nullable=False)
    item = relationship('ItemDB')
    createAt = Column(DATETIME, unique=False, nullable=False)

class LogDB(Model):
    __tablename__ = 'logs'
    id = Column(MEDIUMINT, primary_key=True, autoincrement=True)
    Personalities = Column(JSON, unique=False, nullable=False)
    description = Column(VARCHAR(255), unique=False, nullable=False)
    values = Column(JSON, unique=False, nullable=False)
    createAt = Column(DATETIME, unique=False, nullable=False)


@client.event
async def on_ready():
    pass


if __name__ == '__main__':
    client.run(config.discord_token)
    engine = create_engine(config.dbUrl)
    DBSession = sessionmaker(binds={Model: engine}, expire_on_commit=False)
    session = DBSession()
    Model.metadata.create_all(engine)
