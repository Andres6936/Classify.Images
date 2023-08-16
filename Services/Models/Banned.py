from peewee import CharField, DecimalField

from Services.Models.BaseModel import BaseModel


class Banned(BaseModel):
    SKU = DecimalField()
    Name = CharField()
    Price = DecimalField()
