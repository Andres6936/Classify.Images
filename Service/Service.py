from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def GetRoot():
    pass


@app.get('/banned/count')
def GetCountBanned():
    pass


@app.get('/products/count')
def GetCountProducts():
    pass


@app.get('/reference/count')
def GetCountReference():
    pass
