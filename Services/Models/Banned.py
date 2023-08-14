from peewee import Model, SqliteDatabase, CharField, DecimalField

db = SqliteDatabase('./Data/SQLite.sqlite')


class Banned(Model):
    SKU = DecimalField()
    Name = CharField()
    Price = DecimalField()

    class Meta:
        database = db
