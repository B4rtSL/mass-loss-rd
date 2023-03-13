import basic_funcs as basf
import numpy as np
import matplotlib.pyplot as plt
import breguet_simple_jet as bsj
import breguet_simple_propeller as bsp

altitude = 0
area = 17.02
aspectratio = 8.7
cx0 = 0.0255
efficiency = 0.8
fuelcons = 0.23
nompow = 290
propnumber =2
proptype = 'propeller'
startmass = 2200
vmax = 150
vmin = 35

breguet1 = bsp.breguetPropeller(startmass, nompow, fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency)
breguet1_velocity = breguet1[0]
breguet1_times = breguet1[1]
breguet1_ranges = breguet1[2]

breguet2 = bsp.breguetPropeller_2set(startmass, nompow, fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency)
breguet2_velocity = breguet2[0]
breguet2_times = breguet2[1]
breguet2_ranges = breguet2[2]

breguet3 = bsp.breguetPropeller_3set(startmass, nompow, fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency)
breguet3_velocity = breguet3[0]
breguet3_times = breguet3[1]
breguet3_ranges = breguet3[2]

'''
fig = plt.figure()
plt.plot(breguet1_velocity, breguet1_times, breguet1_velocity, breguet1_ranges)
fig2 = plt.figure()
plt.plot(breguet2_velocity, breguet2_times, breguet2_velocity, breguet2_ranges)
fig3 = plt.figure()
plt.plot(breguet3_velocity, breguet3_times, breguet3_velocity, breguet3_ranges)
'''

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