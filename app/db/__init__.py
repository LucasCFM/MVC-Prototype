'''
Instantiate a DATABASE

https://github.com/coleifer/peewee
'''

from peewee import *

from app.config import Config


CONFIG = Config().config_vars
db = SqliteDatabase(CONFIG.DB_NAME)


from app.models.message import Message


db.connect()
db.create_tables( [Message] )
