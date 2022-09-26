from loader import bot
from core import config

from utils import logging

if __name__ == '__main__':
    logging.create_logging(path = config.logs.path)
    bot.run(config.bot.token)