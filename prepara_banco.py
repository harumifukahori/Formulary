from datetime import datetime

from flask import PostgreSQL
from peewee import *

db = PostgreSQL()


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    nome = TextField()
    nickname = TextField(unique=True)
    senha = TextField()


class Grupo(BaseModel):
    nome = TextField()
    dona = ForeignKeyField(Pessoa, backref='grupos')


class Jogos(BaseModel):
    dona = ForeignKeyField(Pessoa, backref='jogos')
    grupo = ForeignKeyField(Grupo, backref='jogos', null=True, default=None)
    titulo = TextField()
    jogos = TextField()
    criado_em = DateTimeField(default=datetime.now)
    modificado_em = DateTimeField()


PostgresqlDatabase.connect()
