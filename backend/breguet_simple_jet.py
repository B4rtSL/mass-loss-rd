import numpy as np
import math
import matplotlib.pyplot as plt
import basic_funcs 

def breguetJet(startmass, nompow_jet,fuelcons_jet,propnumber,altitude,aspectratio,cx0,area,vmin,vmax):
    
    #Air density from SI
    air_density=1.2255*(1-(altitude/44300))**4.256

    #masses needed in calculations
    difmass_jet=propnumber*nompow_jet*fuelcons_jet*1.25    
    fuelmass_jet=0.35*startmass-difmass_jet                 
    endmass_jet=startmass-fuelmass_jet                             

    #array of velocities, counting step - 100
    x=np.linspace(vmin,vmax,100)
    
    #creating empty arrays for further calculations
    times=[]
    ranges=[]

    #loop calculations of Breguet formulas
    for i in x:
        A_factor=air_density*area*i*i*math.sqrt(cx0*3.14*aspectratio)
        time=10*(1/9.81/fuelcons_jet)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*startmass/A_factor)-math.atan(2*9.81*endmass_jet/A_factor))
        range=3.6*i*time
        times.append(time)
        ranges.append(range)
    
    times_arr=100*np.array(times)     
    ranges_arr=np.array(ranges)    

    #preparing lists of needed values
    x_list=list(x*3.6)
    times_list=list(times_arr)    
    ranges_list=list(ranges_arr) 
  
    #returning dictionary, as this is form needed by Plotly
    return_dict={
        'times_list':times_list,
        'ranges_list':ranges_list,
        'x_list':x_list
    }

    return return_dict

def breguetJet2(startmass, nompow_jet,fuelcons_jet,propnumber,altitude,aspectratio,cx0,area,vmin,vmax):
    
    #Air density from SI
    air_density=1.2255*(1-(altitude/44300))**4.256

    #masses needed in calculations
    difmass_jet=propnumber*nompow_jet*fuelcons_jet*1.25    
    fuelmass_jet=0.35*startmass-difmass_jet                 
    endmass_jet=startmass-fuelmass_jet                             

    #array of velocities, counting step - 100
    x=np.linspace(vmin,vmax,100)
    
    #creating empty arrays for further calculations
    times=[]
    ranges=[]

    #loop calculations of Breguet formulas
    for i in x:
        A_factor=air_density*area*i*i*math.sqrt(cx0*3.14*aspectratio)
        time=10*(1/9.81/fuelcons_jet)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*startmass/A_factor)-math.atan(2*9.81*endmass_jet/A_factor))
        range=3.6*i*time
        times.append(time)
        ranges.append(range)
    
    times_arr=100*np.array(times)     
    ranges_arr=np.array(ranges)    

    #preparing lists of needed values
    x_list=list(x*3.6)
    times_list=list(times_arr)    
    ranges_list=list(ranges_arr) 
  
    #returning dictionary, as this is form needed by Plotly
    return_dict={
        'times_list':times_list,
        'ranges_list':ranges_list,
        'x_list':x_list
    }

    return return_dict

def breguetJet3(startmass, nompow_jet,fuelcons_jet,propnumber,altitude,aspectratio,cx0,area,vmin,vmax):
    
    #Air density from SI
    air_density=1.2255*(1-(altitude/44300))**4.256

    #masses needed in calculations
    difmass_jet=propnumber*nompow_jet*fuelcons_jet*1.25    
    fuelmass_jet=0.35*startmass-difmass_jet                 
    endmass_jet=startmass-fuelmass_jet                             

    #array of velocities, counting step - 100
    x=np.linspace(vmin,vmax,100)
    
    #creating empty arrays for further calculations
    times=[]
    ranges=[]

    #loop calculations of Breguet formulas
    for i in x:
        A_factor=air_density*area*i*i*math.sqrt(cx0*3.14*aspectratio)
        time=10*(1/9.81/fuelcons_jet)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*startmass/A_factor)-math.atan(2*9.81*endmass_jet/A_factor))
        range=3.6*i*time
        times.append(time)
        ranges.append(range)
    
    times_arr=100*np.array(times)     
    ranges_arr=np.array(ranges)    

    #preparing lists of needed values
    x_list=list(x*3.6)
    times_list=list(times_arr)    
    ranges_list=list(ranges_arr) 
  
    #returning dictionary, as this is form needed by Plotly
    return_dict={
        'times_list':times_list,
        'ranges_list':ranges_list,
        'x_list':x_list
    }

    return return_dict
    