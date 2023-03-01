from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import breguet_simple_jet as bsj
import breguet_simple_propeller as bsp

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
    
    returned_dictProp1 = bsp.breguetPropeller(object.startmass, object.nompow, object.fuelcons, object.propnumber, object.altitude, object.aspectratio, object.cx0, object.area, object.vmin, object.vmax, object.efficiency)
    returned_dictJet1 = bsj.breguetJet(object.startmass,object.nompow,object.fuelcons,object.propnumber,object.altitude,object.aspectratio,object.cx0,object.area,object.vmin,object.vmax)
    returned_dictProp2 = bsp.breguetPropeller_2set(object.startmass, object.nompow, object.fuelcons, object.propnumber, object.altitude, object.aspectratio, object.cx0, object.area, object.vmin, object.vmax, object.efficiency)
    returned_dictJet2 = bsj.breguetJet_2set(object.startmass,object.nompow,object.fuelcons,object.propnumber,object.altitude,object.aspectratio,object.cx0,object.area,object.vmin,object.vmax)
    returned_dictProp3 = bsp.breguetPropeller_3set(object.startmass, object.nompow, object.fuelcons, object.propnumber, object.altitude, object.aspectratio, object.cx0, object.area, object.vmin, object.vmax, object.efficiency)
    returned_dictJet3 = bsj.breguetJet_3set(object.startmass,object.nompow,object.fuelcons,object.propnumber,object.altitude,object.aspectratio,object.cx0,object.area,object.vmin,object.vmax)
    if object.proptype == 'propeller':
        return [{
            'x': returned_dictProp1['x_list'],
            'y' : returned_dictProp1['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictProp1['x_list'],
            'y' : returned_dictProp1['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    elif object.proptype == 'propeller-set-2':
        return [{
            'x': returned_dictProp2['x_list'],
            'y' : returned_dictProp2['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictProp2['x_list'],
            'y' : returned_dictProp2['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    elif object.proptype == 'propeller-set-3':
        return [{
            'x': returned_dictProp3['x_list'],
            'y' : returned_dictProp3['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictProp3['x_list'],
            'y' : returned_dictProp3['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    elif object.proptype == 'jet':
        return [{
            'x': returned_dictJet1['x_list'],
            'y' : returned_dictJet1['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictJet1['x_list'],
            'y' : returned_dictJet1['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    elif object.proptype == 'jet-set-2':
        return [{
            'x': returned_dictJet2['x_list'],
            'y' : returned_dictJet2['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictJet2['x_list'],
            'y' : returned_dictJet2['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]
    elif object.proptype == 'jet-set-3':
        return [{
            'x': returned_dictJet3['x_list'],
            'y' : returned_dictJet3['times_list'],
            'type': 'line',
            'name': '100*T [h]'
        },{
            'x': returned_dictJet3['x_list'],
            'y' : returned_dictJet3['ranges_list'],
            'type': 'line',
            'name': 'L [km]'
        }]    
    



