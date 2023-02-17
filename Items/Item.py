from ModelDB import MInvItem, MItem, session
from sqlalchemy.exc import NoResultFound


class Item:
    def __init__(self):
        self.MInvItem = self.__check_MInvItem()
    
    def __check_MInvItem(self):
        result = session.query(MInvItem).where(MInvItem._user_id == self.id).all()
        return result if len(result) != 0 else None

# GETTERS
    @property
    def id(self):
        return self.MInvItem._id

    @property
    def user_id(self):
        return self.MInvItem._user_id

    @property
    def item_id(self):
        return self.MInvItem._item_id

    @property
    def create_at(self):
        return self.MInvItem._create_at

# SETTERS
    @id.setter
    def id(self, value):
        self.MInvItem._id = value
        session.commit()

    @user_id.setter
    def user_id(self, value):
        self.MInvItem._user_id = value
        session.commit()

    @item_id.setter
    def item_id(self, value):
        self.MInvItem._item_id = value
        session.commit()

    @create_at.setter
    def create_at(self, value):
        self.MInvItem._create_at = value
        session.commit()
