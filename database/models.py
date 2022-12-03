from tortoise import fields
from database.base import BaseModel

class User(BaseModel):
    guild_id = fields.BigIntField()
    user_id = fields.BigIntField()

    class Meta:
        table = 'users'