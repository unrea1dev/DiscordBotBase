from misc import AbstractConfiuration

class Bot(AbstractConfiuration):
    token : str = 'Bot token here'
    prefix : str = '!'
    cogs : list[str] = ['cogs.bot.events', 'cogs.user.events']

class Database(AbstractConfiuration):
    database : str = 'sqlite://database.db'

class Logging(AbstractConfiuration):
    path : str = 'log.log'

class Config(AbstractConfiuration):
    bot : Bot = Bot()
    database : Database = Database()
    logging : Logging = Logging()