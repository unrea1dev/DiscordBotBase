import asyncio, signal, logging, os
from nextcord.ext.commands import Bot, Cog

import database
from core import config

class Bot_Events(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot
        signal.signal(signal.SIGINT, self.close_handler)
    
    def close_handler(self, signal, frame) -> None:
        loop = asyncio.get_event_loop()
        loop.create_task(self.on_close())

    @Cog.listener()
    async def on_ready(self) -> None:
        await database.create_connection(url = config.database.database)
        logging.info('Bot started')

    async def on_close(self) -> None:
        await database.close_connection()
        logging.info('Bot closed')
        os._exit(0)

def setup(bot : Bot):
    bot.add_cog(Bot_Events(bot))
