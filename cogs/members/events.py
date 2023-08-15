import nextcord
from nextcord.ext.commands import Bot, Cog

from database.models import Member

class MemberEvents(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member : nextcord.Member) -> None:
        new_member = await Member.filter(guild_id = member.guild.id, member_id = member.id).first()
        if not new_member:
            await Member.create(guild_id = member.guild.id, member_id = member.id)
            
def setup(bot : Bot):
    bot.add_cog(MemberEvents(bot))