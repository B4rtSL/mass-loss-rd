import basic_funcs as basf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import breguet_simple_propeller as bsp
from data_container import Cessna150

aero_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

eta_prep = basf.eta_prep(eta_input)
eta_velo = eta_prep[0]
eta = eta_prep[1]

newfilepath = Path('C:/Users/barto/Desktop/inżynierka/test-data/test-results/data.csv')

altitude = 762
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
air_density=1.2255*(1-(altitude/44300))**4.256

breguet100 = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet100_velocity = breguet100[0]
breguet100_times = breguet100[1]
breguet100_ranges = breguet100[2]

breguet75 = bsp.breguetPropeller(0.75*startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet75_velocity = breguet75[0]
breguet75_times = breguet75[1]
breguet75_ranges = breguet75[2]

breguet50 = bsp.breguetPropeller(0.5*startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet50_velocity = breguet50[0]
breguet50_times = breguet50[1]
breguet50_ranges = breguet50[2]

fig2 = plt.figure()
plt.plot(breguet100_velocity, breguet100_ranges, "--r" , label = "100% Start Mass Range")
plt.plot(breguet75_velocity, breguet75_ranges,"-b" , label = "75% Start Mass Range")
plt.plot(breguet50_velocity, breguet50_ranges, "-.g" , label = "50% Start Mass Range")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range vs Velocity - Start Mass Sensitivity")
plt.grid(which='both', axis='both')


fig3 = plt.figure()
plt.plot(breguet100_velocity, breguet100_times, "--r" , label = "100% Start Mass Endurance")
plt.plot(breguet75_velocity, breguet75_times,"-b" , label = "75% Start Mass Endurance")
plt.plot(breguet50_velocity, breguet50_times, "-.g" , label = "50% Start Mass Endurance")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h]")
plt.title("Endurance vs Velocity - Start Mass Sensitivity")
plt.grid(which='both', axis='both')

breguet100fm = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet100fm_velocity = breguet100fm[0]
breguet100fm_times = breguet100fm[1]
breguet100fm_ranges = breguet100fm[2]

breguet75fm = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, 0.75*fuelmass, aero_input)
breguet75fm_velocity = breguet75fm[0]
breguet75fm_times = breguet75fm[1]
breguet75fm_ranges = breguet75fm[2]

breguet50fm = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, 0.5*fuelmass, aero_input)
breguet50fm_velocity = breguet50fm[0]
breguet50fm_times = breguet50fm[1]
breguet50fm_ranges = breguet50fm[2]

fig4 = plt.figure()
plt.plot(breguet100fm_velocity, breguet100fm_ranges, "--r" , label = "100% Fuel Mass Range")
plt.plot(breguet75fm_velocity, breguet75fm_ranges,"-b" , label = "75% Fuel Mass Range")
plt.plot(breguet50fm_velocity, breguet50fm_ranges, "-.g" , label = "50% Fuel Mass Range")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range vs Velocity - Fuel Mass Sensitivity")
plt.grid(which='both', axis='both')


fig5 = plt.figure()
plt.plot(breguet100fm_velocity, breguet100fm_times, "--r" , label = "100% Fuel Mass Endurance")
plt.plot(breguet75fm_velocity, breguet75fm_times,"-b" , label = "75% Fuel Mass Endurance")
plt.plot(breguet50fm_velocity, breguet50fm_times, "-.g" , label = "50% Fuel Mass Endurance")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h]")
plt.title("Endurance vs Velocity - Fuel Mass Sensitivity")
plt.grid(which='both', axis='both')

breguet100eff = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet100eff_velocity = breguet100eff[0]
breguet100eff_times = breguet100eff[1]
breguet100eff_ranges = breguet100eff[2]

breguet80eff = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, 0.8*efficiency, fuelmass, aero_input)
breguet80eff_velocity = breguet80eff[0]
breguet80eff_times = breguet80eff[1]
breguet80eff_ranges = breguet80eff[2]

breguet120eff = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, 1.2*efficiency, fuelmass, aero_input)
breguet120eff_velocity = breguet120eff[0]
breguet120eff_times = breguet120eff[1]
breguet120eff_ranges = breguet120eff[2]

fig6 = plt.figure()
plt.plot(breguet120eff_velocity, breguet120eff_ranges, "--r" , label = "120% of Average Efficiency")
plt.plot(breguet100eff_velocity, breguet100eff_ranges,"-b" , label = "100% of Average Efficiency")
plt.plot(breguet80eff_velocity, breguet80eff_ranges, "-.g" , label = "80% of Average Efficiency")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range vs Velocity - Efficiency Sensitivity")
plt.grid(which='both', axis='both')


fig7 = plt.figure()
plt.plot(breguet120eff_velocity, breguet120eff_ranges, "--r" , label = "120% of Average Efficiency")
plt.plot(breguet100eff_velocity, breguet100eff_ranges,"-b" , label = "100% of Average Efficiency")
plt.plot(breguet80eff_velocity, breguet80eff_ranges, "-.g" , label = "80% of Average Efficiency")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h]")
plt.title("Endurance vs Velocity - Efficiency Sensitivity")
plt.grid(which='both', axis='both')

breguet100sfc = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet100sfc_velocity = breguet100sfc[0]
breguet100sfc_times = breguet100sfc[1]
breguet100sfc_ranges = breguet100sfc[2]

breguet80sfc = bsp.breguetPropeller(startmass, nompow, 0.8*avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet80sfc_velocity = breguet80sfc[0]
breguet80sfc_times = breguet80sfc[1]
breguet80sfc_ranges = breguet80sfc[2]

breguet120sfc = bsp.breguetPropeller(startmass, nompow, 1.2*avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet120sfc_velocity = breguet120sfc[0]
breguet120sfc_times = breguet120sfc[1]
breguet120sfc_ranges = breguet120sfc[2]

fig8 = plt.figure()
plt.plot(breguet120sfc_velocity, breguet120sfc_ranges, "--r" , label = "120% of Average SFC")
plt.plot(breguet100sfc_velocity, breguet100sfc_ranges,"-b" , label = "100% of Average SFC")
plt.plot(breguet80sfc_velocity, breguet80sfc_ranges, "-.g" , label = "80% of Average SFC")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range vs Velocity - SFC Sensitivity")
plt.grid(which='both', axis='both')


fig9 = plt.figure()
plt.plot(breguet120sfc_velocity, breguet120sfc_times, "--r" , label = "120% of Average SFC")
plt.plot(breguet100sfc_velocity, breguet100sfc_times,"-b" , label = "100% of Average SFC")
plt.plot(breguet80sfc_velocity, breguet80sfc_times, "-.g" , label = "80% of Average SFC")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h]")
plt.title("Endurance vs Velocity - SFC Sensitivity")
plt.grid(which='both', axis='both')

plt.show()
