import nextcord
from nextcord.ext.commands import Bot, Cog

from database.models import User

class User_Events(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member : nextcord.Member) -> None:
        user = await User.filter(guild_id = member.guild.id, user_id = member.id).first()
        if not user:
            user = await User.create(guild_id = member.guild.id, user_id = member.id)
            
def setup(bot : Bot):
    bot.add_cog(User_Events(bot))
