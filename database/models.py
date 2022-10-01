from tortoise import fields
from database.base import BaseModel

class User(BaseModel):
    guild_id = fields.BigIntField()
    user_id = fields.BigIntField()

    class Meta:
        table = 'users'

    def __str__(self) -> str:
        return str(
            {
                'id' : self.id,
                'guild_id' : self.guild_id,
                'user_id' : self.user_id
            }
        )