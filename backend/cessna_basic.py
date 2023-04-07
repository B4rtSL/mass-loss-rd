import basic_funcs as basf
import numpy as np
import matplotlib.pyplot as plt
import breguet_simple_propeller as bsp
from data_container import Cessna150

aero_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

eta_prep = basf.eta_prep(eta_input)
eta_velo = eta_prep[0]
eta = eta_prep[1]


altitude = 0
efficiency = 0.8
area = Cessna150.area
aspectratio = Cessna150.aspectratio
cx0 = Cessna150.cx0
avg_fuelcons = Cessna150.fuelcons
nompow = Cessna150.nompow
propnumber = Cessna150.propnumber
proptype = 'propeller'
startmass = Cessna150.startmass
vmax = Cessna150.vmax
vmin = Cessna150.vmin
fuelmass = Cessna150.fuelmass

breguet1 = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass)
breguet1_velocity = breguet1[0]
breguet1_times = breguet1[1]
breguet1_ranges = breguet1[2]

breguet2 = bsp.breguetPropeller_2set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet2_velocity = breguet2[0]
breguet2_times = breguet2[1]
breguet2_ranges = breguet2[2]

breguet3 = bsp.breguetPropeller_3set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency,fuelmass, aero_input)
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
plt.plot(breguet1_velocity, breguet1_times, "--r" , label = "Breguet-endurance-propeller-1")
plt.plot(breguet2_velocity, breguet2_times,"-b" , label = "Breguet-endurance-propeller-2")
plt.plot(breguet3_velocity, breguet3_times, "-.g" , label = "Breguet-endurance-propeller-3")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Time [100h]")
plt.title("Endurance on Velocity")


fig5 = plt.figure()
plt.plot(breguet1_velocity, breguet1_times, label = "Breguet-endurance-propeller-1")
plt.plot(breguet1_velocity, breguet1_ranges, label = "Breguet-range-propeller-1")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h] and Range [km]")
plt.show()