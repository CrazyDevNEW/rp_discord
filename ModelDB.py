import datetime
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
    BOOLEAN,
    DATETIME,
    ENUM,
    JSON,
    TEXT)
import config


class Base(DeclarativeBase):
    pass


class User(Base):  # TODO Инициальзация модели бд
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(MEDIUMINT, primary_key=True, autoincrement=True)
    discord_id: Mapped[int] = mapped_column(BIGINT, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(TEXT(50), unique=False, nullable=False)
    last_name: Mapped[str] = mapped_column(TEXT(50), unique=False, nullable=False)
    nationality: Mapped[str] = mapped_column(TEXT(50), unique=False, nullable=False, default="Russia")
    description: Mapped[str] = mapped_column(TEXT(1000), unique=False, nullable=False)
    skin: Mapped[dict] = mapped_column(JSON, unique=False, nullable=False)
    experience: Mapped[str] = mapped_column(BIGINT, unique=False, nullable=False)
    game_currency: Mapped[int] = mapped_column(BIGINT, unique=False, nullable=False)
    real_currency: Mapped[int] = mapped_column(BIGINT, unique=False, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DATETIME, unique=False, nullable=False)
    latest_in_game: Mapped[datetime] = mapped_column(DATETIME, unique=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


class Invetory(Base):  # TODO Инициальзация модели бд
    __tablename__ = "inventories"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    item: Mapped["Item"] = relationship()
    create_at: Mapped[datetime] = mapped_column(DATETIME, unique=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


class Item(Base):  # TODO Инициальзация модели бд
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    item_type: Mapped[str] = mapped_column(TEXT, unique=False, nullable=False)
    name: Mapped[str] = mapped_column(TEXT, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(TEXT, unique=False, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DATETIME, unique=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


class Player(Base):  # TODO Инициальзация модели бд
    __tablename__ = "players"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()
    heal_points: Mapped[int] = mapped_column(TINYINT, unique=False, nullable=False, default=100)
    armor_points: Mapped[int] = mapped_column(TINYINT, unique=False, nullable=False, default=100)
    effects: Mapped[dict] = mapped_column(JSON, unique=False, nullable=False)
    position: Mapped[dict] = mapped_column(JSON, unique=False, nullable=False)
    join_at: Mapped[datetime] = mapped_column(DATETIME, unique=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


engine = create_engine(config.dbUrl)
session = Session(engine)
Base.metadata.create_all(engine)
