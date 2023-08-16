from fastapi import FastAPI

from Services.Models.Banned import Banned
from Services.Models.Products import Products
from Services.Models.Reference import Reference

app = FastAPI()


@app.get('/')
def GetRoot():
    return {'Hello': 'World'}


@app.get('/banned/count')
def GetCountBanned():
    count = Banned.select().count()
    return {'Count': count}


@app.get('/products/count')
def GetCountProducts():
    count = Products.select().count()
    return {'Count': count}


@app.get('/reference/count')
def GetCountReference():
    count = Reference.select().count()
    return {'Count': count}
