from fastapi import FastAPI
import json

#function to retrive the data 
def load_data():
    with open('patient.json','r') as file:
        data=json.load(file)
    return data
#creating the demo api server

app=FastAPI()

@app.get('/')
def hello():
    return {'message':'Welcome to Patient Management System Usig Fast API '}
    
#creating the about 
@app.get('/about')
def about():
    return{'message':'This is the fully functional API for the Patient Management Application'}

#creating the view page
@app.get('/view')
def view():
    data=load_data()
    return data
