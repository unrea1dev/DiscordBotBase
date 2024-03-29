from loader import bot
from core import config

from misc.logs import initialize_logging

if __name__ == '__main__':
    initialize_logging(path = config.logging.path)
    bot.run(config.bot.token)