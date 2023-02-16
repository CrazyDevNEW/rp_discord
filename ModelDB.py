import datetime
import time

from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.dialects.mysql import (
    BIGINT,
    MEDIUMINT,
    TINYINT,
    DATETIME,
    JSON,
    TEXT)
import config


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        return f"{self.__dict__}"


class MUser(Base):  # Инициальзация модели бд
    __tablename__ = "users"
    _id: Mapped[int] = mapped_column("id", MEDIUMINT, primary_key=True, autoincrement=True)
    _discord_id: Mapped[int] = mapped_column("discord_id", BIGINT, unique=True, nullable=False)
    _first_name: Mapped[str] = mapped_column("first_name", TEXT(50), unique=False, nullable=False)
    _last_name: Mapped[str] = mapped_column("last_name", TEXT(50), unique=False, nullable=False)
    _nationality: Mapped[str] = mapped_column("nationality", TEXT(50), unique=False, nullable=False, default="Russia")
    _description: Mapped[str] = mapped_column("description", TEXT(1000), unique=False, nullable=False)
    _skin: Mapped[dict] = mapped_column("skin", JSON, unique=False, nullable=False, default={})
    _experience: Mapped[str] = mapped_column("experience", BIGINT, unique=False, nullable=False, default=0)
    _game_currency: Mapped[int] = mapped_column("game_currency", BIGINT, unique=False, nullable=False, default=0)
    _real_currency: Mapped[int] = mapped_column("real_currency", BIGINT, unique=False, nullable=False, default=0)
    _create_at: Mapped[datetime] = mapped_column("create_at", DATETIME, unique=False, nullable=False, default=datetime.datetime.now())
    _latest_in_game: Mapped[datetime] = mapped_column("latest_in_game", DATETIME, unique=False, nullable=False, default=datetime.datetime.now())


class MInvetory(Base):  # Инициальзация модели бд
    __tablename__ = "inventories"
    _id: Mapped[int] = mapped_column("id", BIGINT, primary_key=True)
    _user_id: Mapped[int] = mapped_column("user_id", ForeignKey("users.id"))
    _user: Mapped["MUser"] = relationship()
    _item_id: Mapped[int] = mapped_column("item_id", ForeignKey("items.id"))
    _item: Mapped["MItem"] = relationship()
    _create_at: Mapped[datetime] = mapped_column("create_at", DATETIME, unique=False, nullable=False)


class MItem(Base):  # Инициальзация модели бд
    __tablename__ = "items"
    _id: Mapped[int] = mapped_column("id", BIGINT, primary_key=True)
    _item_type: Mapped[str] = mapped_column("item_type", TEXT, unique=False, nullable=False)
    _name: Mapped[str] = mapped_column("name", TEXT, unique=False, nullable=False)
    _description: Mapped[str] = mapped_column("description", TEXT, unique=False, nullable=False)
    _create_at: Mapped[datetime] = mapped_column("create_at", DATETIME, unique=False, nullable=False)


class MPlayer(Base):  # Инициальзация модели бд
    __tablename__ = "players"
    _id: Mapped[int] = mapped_column("id", BIGINT, primary_key=True)
    _user_id: Mapped[int] = mapped_column("user_id", ForeignKey("users.id"))
    _user: Mapped["MUser"] = relationship()
    _heal_points: Mapped[int] = mapped_column("heal_points", TINYINT, unique=False, nullable=False, default=100)
    _armor_points: Mapped[int] = mapped_column("armor_points", TINYINT, unique=False, nullable=False, default=100)
    _effects: Mapped[dict] = mapped_column("effects", JSON, unique=False, nullable=False)
    _position: Mapped[dict] = mapped_column("position", JSON, unique=False, nullable=False)
    _join_at: Mapped[datetime] = mapped_column("join_at", DATETIME, unique=False, nullable=False)


engine = create_engine(config.dbUrl)
session = Session(engine)
Base.metadata.create_all(engine)
