from ModelDB import MUser
from Player.GetterSetter import _GetSet
import discord


class User(_GetSet):
    def __init__(self, member: discord.Member, **kwargs):
        self.member = member
        super().__init__()

    def __str__(self) -> str:
        pass

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass