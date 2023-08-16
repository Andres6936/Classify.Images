from peewee import CharField, DecimalField, IntegerField

from Services.Models.BaseModel import BaseModel


class Reference(BaseModel):
    NameDATE = CharField()
    City = CharField()
    Davipola = IntegerField()
    SKU = DecimalField()
    Name = CharField()
    Measure = CharField()
    Branch = CharField()
    AmountSells = DecimalField()
    Participation = CharField()
    PriceImplicit = DecimalField()
    PriceReport = DecimalField()
