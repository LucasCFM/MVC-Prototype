from peewee import *

from app.db import db


'''
https://github.com/coleifer/peewee
'''


class BaseModel(Model):
    class Meta:
        database = db


class Message(BaseModel):
    id = PrimaryKeyField(unique=True)
    content = TextField()
    
    def __str__(self):
        return f'{self.id}: {self.content}'

    def __hash__(self):
        return hash((self.__class__, self._get_pk_value()))
    
    @property
    def _hash(self):
        return self.__hash__()
