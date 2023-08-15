from nextcord import Intents
from nextcord.ext.commands import Bot

from core import config

bot = Bot(intents = Intents.all())

for cog in config.bot.cogs:
    bot.load_extension(cog)