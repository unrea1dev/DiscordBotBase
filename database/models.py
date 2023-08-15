from tortoise import fields
from database.base import BaseModel

class Member(BaseModel):
    guild_id = fields.BigIntField()
    member_id = fields.BigIntField()
    created_at = fields.DatetimeField(auto_now_add = True)

    class Meta:
        table = 'members'