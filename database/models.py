from tortoise.models import Model
from tortoise import fields

class BaseModel(Model):
    id = fields.IntField(pk = True)

    def __repr__(self) -> str:
        return '<{}{}>'.format(self.__class__.__name__, self.__str__())

class BaseModel(BaseModel):
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