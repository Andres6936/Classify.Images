from fastapi import FastAPI

from Services.Models.Banned import Banned

app = FastAPI()


@app.get('/')
def GetRoot():
    return {'Hello': 'World'}


@app.get('/banned/count')
def GetCountBanned():
    count = Banned.select().count()
    return {'count': count}


@app.get('/products/count')
def GetCountProducts():
    pass


@app.get('/reference/count')
def GetCountReference():
    pass
