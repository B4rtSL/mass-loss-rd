import basic_funcs as basf
import numpy as np
import matplotlib.pyplot as plt
import breguet_simple_propeller as bsp
from data_container import Hawker

aero_input = 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx'
altitude = 0
efficiency = 0.8
area = Hawker.area
aspectratio = Hawker.aspectratio
cx0 = Hawker.cx0
avg_fuelcons = Hawker.fuelcons
nompow = Hawker.nompow
propnumber = Hawker.propnumber
proptype = 'propeller'
startmass = Hawker.startmass
vmax = Hawker.vmax
vmin = Hawker.vmin

breguet1 = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency)
breguet1_velocity = breguet1[0]
breguet1_times = breguet1[1]
breguet1_ranges = breguet1[2]

breguet2 = bsp.breguetPropeller_2set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, aero_input)
breguet2_velocity = breguet2[0]
breguet2_times = breguet2[1]
breguet2_ranges = breguet2[2]

breguet3 = bsp.breguetPropeller_3set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, aero_input)
breguet3_velocity = breguet3[0]
breguet3_times = breguet3[1]
breguet3_ranges = breguet3[2]

fig4 = plt.figure()
plt.plot(breguet1_velocity, breguet1_ranges, "--r" , label = "Breguet-range-propeller-1")
plt.plot(breguet2_velocity, breguet2_ranges,"-b" , label = "Breguet-range-propeller-2")
plt.plot(breguet3_velocity, breguet3_ranges, "-.g" , label = "Breguet-range-propeller-3")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range on Velocity")

fig5 = plt.figure()
plt.plot(breguet1_velocity, breguet1_times, "--r" , label = "Breguet-time-propeller-1")
plt.plot(breguet2_velocity, breguet2_times,"-b" , label = "Breguet-time-propeller-2")
plt.plot(breguet3_velocity, breguet3_times, "-.g" , label = "Breguet-time-propeller-3")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Time [100h]")
plt.title("Endurance on Velocity")
plt.show()