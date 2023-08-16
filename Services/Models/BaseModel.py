from peewee import Model, SqliteDatabase

db = SqliteDatabase('./Data/SQLite.sqlite')


class BaseModel(Model):
    class Meta:
        database = db
