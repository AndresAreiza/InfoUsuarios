from typing import Union
from fastapi import FastAPI
import requests
from pydantic import BaseModel
from typing import Optional
import json
import logging
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'infoUsers.log',
    filemode='w'
)

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def getInfoUsers():
    data=''
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/infoUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    if data != '' and data != 'Not found':
        logging.info('GET method executed successfully')
        return {"infoUsers": response.json()}
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: No Content"}

@app.get("/infoUsers/idUsuario={idUsuario}")
def read_infoUsers(idUsuario: str):
    url = 'https://62ffa01534344b6431fdd472.mockapi.io/api/infoUsers'
    response = requests.get(url, {}, timeout=5)
    data = json.loads(response.content)
    wInternalId = ''
    for usr in data:
        if usr['idUsuario'] == idUsuario:
            wInternalId = usr['internalId']    
    if wInternalId != '' and wInternalId != 'Not found':
        logging.info('GET method executed successfully')
        return {"internalId": wInternalId}
    else:
        logging.error('Failed to execute GET method')
        return {"HTTP status code 204: NoContent"}