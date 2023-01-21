from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from breguet_simple_jet import breguetJet
from breguet_simple_propeller import breguetPropeller
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000/"]

class MyForm(BaseModel):
    altitude: float
    area: float
    aspectratio: float
    cx0:float
    efficiency:float
    fuelcons:float
    nompow:float
    propnumber:float
    proptype:str
    startmass:float
    vmax:float
    vmin:float


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def home(object: MyForm):
    
    returned_dictProp=breguetPropeller(object.startmass,object.nompow,object.fuelcons,object.propnumber,object.altitude,object.aspectratio,object.cx0,object.area,object.vmin,object.vmax,object.efficiency)
    returned_dictJet=breguetJet(object.startmass,object.nompow,object.fuelcons,object.propnumber,object.altitude,object.aspectratio,object.cx0,object.area,object.vmin,object.vmax)
    if object.proptype == 'propeller':
        return [{
            'x': returned_dictProp['x_list'],
            'y' : returned_dictProp['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictProp['x_list'],
            'y' : returned_dictProp['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    else:
        return [{
            'x': returned_dictJet['x_list'],
            'y' : returned_dictJet['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictJet['x_list'],
            'y' : returned_dictJet['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    



