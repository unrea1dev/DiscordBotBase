from utils import ConfigStructure

class Bot(ConfigStructure):
    token : str = 'Bot token here'
    prefix : str = '!'
    cogs : list[str] = ['cogs.bot.events', 'cogs.user.events']

class Database(ConfigStructure):
    database : str = 'sqlite://database.db'

class Logging(ConfigStructure):
    path : str = 'log.log'

class Config(ConfigStructure):
    bot : Bot = Bot()
    database : Database = Database()
    logging : Logging = Logging()