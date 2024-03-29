import logging
from nextcord.ext.commands import Bot, Cog

from core import config
import database

from misc.misc import setup_misc

class BotEvents(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

        self.original_close = self.bot.close
        self.bot.close = self.on_disconnect

    @Cog.listener()
    async def on_ready(self) -> None:
        logging.info('Bot connected. Latency {} ms!'.format(round(self.bot.latency, 2)))
        
        await database.create_connection(
            url = config.database.database, 
            timezone = config.database.timezone
        )

        await setup_misc(bot = self.bot)

        logging.info('Bot is running')

    async def on_disconnect(self) -> None:
        await database.close_connection()
        await self.original_close()

def setup(bot : Bot):
    bot.add_cog(BotEvents(bot))
