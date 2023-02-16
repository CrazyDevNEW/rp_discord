from ModelDB import MUser
from Player.GetSet import _GetSet, session
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
        del self.MUser
