from peewee import CharField, DecimalField, IntegerField

from Services.Models.BaseModel import BaseModel


class Products(BaseModel):
    NameDANE = CharField()
    SKU = DecimalField()
    Name = CharField()
    Measure = CharField()
    Branch = CharField()
    Entity = CharField()
    Davipola = IntegerField()
    City = CharField()
    PriceImplicit = DecimalField()
    PriceReport = DecimalField()
