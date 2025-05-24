from fastapi import FastAPI

#creating the demo api server

app=FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello world '}
    print('Hello World')