import Item.Item
from ModelDB import MUser, MInvetory
from Player.GetSet import _GetSet, session
from Item.Item import Item
import discord


class User(_GetSet):
    def __init__(self, member: discord.Member, **kwargs):
        self.member = member
        super().__init__()

    def create(self, **kwargs):
        user = MUser(
            _discord_id=self.member.id,
            _first_name=kwargs.get("first_name"),
            _last_name=kwargs.get("last_name"),
            _nationality=kwargs.get("nationality"),
            _description=kwargs.get("description")
        )
        session.add(user)
        session.commit()
        super().__init__()

    def delete(self):
        session.delete(self.MUser)
        session.commit()
        super().__init__()

    def add_item(self, item: Item):
        added_item = MInvetory(
            _user_id=self.id,
            _item_id=item.id
        )
        session.add(added_item)
        session.commit()

