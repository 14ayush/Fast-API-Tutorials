from fastapi import FastAPI ,Path,HTTPException,Query
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
#now insted of all the patient data i want to retrive the particular patient data 
@app.get('/patient/{patient_id}')
def patient_load(patient_id:str =Path(...,description='Required Patient Id',example='1')):
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    #return {'Error':'Patient not found'} it produce the status code 200 means success but user not get the data
    #so we use the http exception 
    raise HTTPException(status_code=404,detail='Data not Found')

#making the sorted function

@app.get('/sort')
def sored_data(sort_by :str=Query(...,description='Sort on the basic of height,weight,bmi'),order_by:str=Query('asc',description='choose asc or dec')):
    valid_feilds=['height','weight','bmi']
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400,detail='error')
    
    if order_by not in ['asc','dec']:
        raise HTTPException(status_code=400,detail='error')
    
    data=load_data()
    sorted_order=True if order_by=='dec' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get('height',0),reverse=sorted_order)
    return sored_data

