from ModelDB import MUser
from ModelDB import session


class GetterSetter(MUser):
    @property
    def id(self):
        return self._id

    @property
    def discord_id(self):
        return self._discord_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def nationality(self):
        return self._nationality

    @property
    def description(self):
        return self._description

    @property
    def skin(self):
        return self._skin

    @property
    def experience(self):
        return self._experience

    @property
    def game_currency(self):
        return self._game_currency

    @property
    def real_currency(self):
        return self._real_currency

    @property
    def create_at(self):
        return self._create_at

    @property
    def latest_in_game(self):
        return self._latest_in_game