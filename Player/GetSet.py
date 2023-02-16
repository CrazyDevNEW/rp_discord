from ModelDB import *
from ModelDB import session
from sqlalchemy.exc import NoResultFound


class _GetSet(MUser):
    def __init__(self):
        super().__init__()
        self.MUser = self.__check()

    def __check(self):
        try:
            return session.query(MUser).where(MUser._discord_id == self.member.id).one()
        except NoResultFound:
            return None

# GETTERS

    @property
    def id(self):
        return self.MUser._id

    @property
    def discord_id(self):
        return self.MUser._discord_id

    @property
    def first_name(self):
        return self.MUser._first_name

    @property
    def last_name(self):
        return self.MUser._last_name

    @property
    def nationality(self):
        return self.MUser._nationality

    @property
    def description(self):
        return self.MUser._description

    @property
    def skin(self):
        return self.MUser._skin

    @property
    def experience(self):
        return self.MUser._experience

    @property
    def game_currency(self):
        return self.MUser._game_currency

    @property
    def real_currency(self):
        return self.MUser._real_currency

    @property
    def create_at(self):
        return self.MUser._create_at

    @property
    def latest_in_game(self):
        return self.MUser._latest_in_game

# SETTERS
    @id.setter
    def id(self, value):
        self.MUser._id = value
        session.commit()

    @discord_id.setter
    def discord_id(self, value):
        self.MUser._discord_id = value
        session.commit()

    @first_name.setter
    def first_name(self, value):
        self.MUser._first_name = value
        session.commit()

    @last_name.setter
    def last_name(self, value):
        self.MUser._last_name = value
        session.commit()

    @nationality.setter
    def nationality(self, value):
        self.MUser._nationality = value
        session.commit()

    @description.setter
    def description(self, value):
        self.MUser._description = value
        session.commit()

    @skin.setter
    def skin(self, value):
        self.MUser._skin = value
        session.commit()

    @experience.setter
    def experience(self, value):
        self.MUser._experience = value
        session.commit()

    @game_currency.setter
    def game_currency(self, value):
        self.MUser._game_currency = value
        session.commit()

    @real_currency.setter
    def real_currency(self, value):
        self.MUser._real_currency = value
        session.commit()

    @create_at.setter
    def create_at(self, value):
        self.MUser._create_at = value
        session.commit()

    @latest_in_game.setter
    def latest_in_game(self, value):
        self.MUser._latest_in_game = value
        session.commit()
