from ModelDB import MItem, session
from sqlalchemy.exc import NoResultFound


class Item:
    def __init__(self, id: int):
        self.MItem = self.__check_item(id)
    
    @staticmethod
    def __check_item(id: int):
        try:
            return session.query(MItem).where(MItem._id == id).one()
        except NoResultFound:
            return None

    @property
    def create_at(self):
        return self.MItem._create_at

# GETTERS
    @property
    def id(self):
        return self.MItem._id

    @property
    def name(self):
        return self.MItem._name

    @property
    def description(self):
        return self.MItem._description

# SETTERS
    @id.setter
    def id(self, value):
        self.MItem._id = value
        session.commit()

    @name.setter
    def name(self, value):
        self.MItem._name = value
        session.commit()

    @description.setter
    def description(self, value):
        self.MItem._description = value
        session.commit()

    @create_at.setter
    def create_at(self, value):
        self.MItem._create_at = value
        session.commit()
