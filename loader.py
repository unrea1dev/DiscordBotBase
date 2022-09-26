from nextcord import Intents
from nextcord.ext import commands

from core import config

bot = commands.Bot(command_prefix = config.bot.prefix, intents = Intents.all())

for cog in config.bot.cogs:
    bot.load_extension(cog)