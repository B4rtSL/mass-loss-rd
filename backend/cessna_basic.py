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

altitude = 2500
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

double_arr = basf.aero_prep(aero_input)
alpha_arr = double_arr[0]
cz_arr = double_arr[1]
alpha_root = basf.poly_root(alpha_arr, cz_arr, 5, basf.cz(704.682812501, air_density, area, vmax))
coeff_arr = np.polyfit(alpha_arr, cz_arr, 5)
new_alph_arr = basf.new_alph_arr(alpha_arr, alpha_root)
new_cz_arr = basf.new_cz_arr(new_alph_arr, coeff_arr)
new_cx_arr = basf.cx_arr(new_cz_arr, cx0, aspectratio)
lift_drag = basf.lift_to_drag(new_cz_arr, new_cx_arr)

diffmass_prop=propnumber*nompow*avg_fuelcons*1.25
fuelmass_prop=fuelmass-diffmass_prop                 
endmass_prop=startmass-fuelmass_prop                            
calc_mass = (startmass + endmass_prop)/2

print('calc mass', calc_mass, 'diffmass', diffmass_prop, 'fuelmass_prop',fuelmass_prop)
# print('Cz dla vmax', basf.cz(704.682812501, air_density, area, vmax))
# print('New Cz arr', new_cz_arr)
# print('V dla Czmax', basf.velocity(650, air_density, area, 1.1502277))

# x=basf.velocity_arr(704.682812501, air_density, area, new_cz_arr)
# print(x)

fig3 = plt.figure()
plt.plot(alpha_arr, cz_arr, "--r" , label = "aero_prep")
plt.plot(new_alph_arr, new_cz_arr,"-b" , label = "alpha_root")
plt.plot(new_alph_arr, np.divide(lift_drag,10), "-.g" , label = "lift_drag/10")
plt.legend(loc="best")
plt.xlabel("AoA [deg]")
plt.ylabel("Lift Coefficient, (Lift/Drag)/10 [-]")
plt.grid(which='both', axis='both')

latex_aoa = np.around(new_alph_arr, decimals=3)
latex_cz = np.around(new_cz_arr, decimals=3)
latex_cx = np.around(new_cx_arr, decimals=3)
latex_LD = np.around(lift_drag, decimals=3)

raw_data = {'AoA [deg]': latex_aoa[0::2],
            'Cz [-]': latex_cz[0::2],
            'Cx [-]': latex_cx[0::2],
            'L/D [-]': latex_LD[0::2]
            }

df = pd.DataFrame(raw_data, columns=['AoA [deg]', 'Cz [-]', 'Cx [-]', 'L/D [-]'])
df.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/results-cz-graph-cessna.csv')

breguet1 = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
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

breguet1_velocity = np.around(breguet1_velocity, decimals=3)
breguet1_ranges = np.around(breguet1_ranges, decimals=3)
breguet1_times = np.around(breguet1_times, decimals=3)

# raw_data = {'velocity': breguet1_velocity[0::4],
#             'range': breguet1_ranges[0::4],
#             'endurance': breguet1_times[0::4]}

# df = pd.DataFrame(raw_data, columns=['velocity', 'range', 'endurance'])
# df.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/data.csv')

fig4 = plt.figure()
plt.plot(breguet1_velocity, breguet1_ranges, "--r" , label = "Breguet-range-1")
plt.plot(breguet2_velocity, breguet2_ranges,"-b" , label = "Breguet-range-2")
plt.plot(breguet3_velocity, breguet3_ranges, "-.g" , label = "Breguet-range-3")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Range [km]")
plt.title("Range vs Velocity")
plt.grid(which='both', axis='both')


fig5 = plt.figure()
plt.plot(breguet1_velocity, breguet1_times, "--r" , label = "Breguet-endurance-1")
plt.plot(breguet2_velocity, breguet2_times,"-b" , label = "Breguet-endurance-2")
plt.plot(breguet3_velocity, breguet3_times, "-.g" , label = "Breguet-endurance-3")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h]")
plt.title("Endurance vs Velocity")
plt.grid(which='both', axis='both')


fig5 = plt.figure()
plt.plot(breguet1_velocity, breguet1_times, label = "Breguet-endurance-propeller-1")
plt.plot(breguet1_velocity, breguet1_ranges, label = "Breguet-range-propeller-1")
plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h] and Range [km]")
plt.title("Range Endurance vs Velocity - 1st Method")
plt.grid(which='both', axis='both')
plt.show()