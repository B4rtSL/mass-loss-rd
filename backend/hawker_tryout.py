import basic_funcs as basf
import numpy as np
import pandas as pd
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
fuelmass = Hawker.fuelmass

double_arr = basf.aero_prep(aero_input)
alpha_arr = double_arr[0]
cz_arr = double_arr[1]
alpha_root = basf.poly_root(alpha_arr, cz_arr, 5, basf.cz(5820.5375, 1.2255, area, vmax))
coeff_arr = np.polyfit(alpha_arr, cz_arr, 5)
new_alph_arr = basf.new_alph_arr(alpha_arr, alpha_root)
new_cz_arr = basf.new_cz_arr(new_alph_arr, coeff_arr)
new_cx_arr = basf.cx_arr(new_cz_arr, cx0, aspectratio)
lift_drag = basf.lift_to_drag(new_cz_arr, new_cx_arr)

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
df.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/results-cz-graph-hawker.csv')


breguet1 = bsp.breguetPropeller(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet1_velocity = breguet1[0]
breguet1_times = breguet1[1]
breguet1_ranges = breguet1[2]

breguet2 = bsp.breguetPropeller_2set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet2_velocity = breguet2[0]
breguet2_times = breguet2[1]
breguet2_ranges = breguet2[2]

breguet3 = bsp.breguetPropeller_3set(startmass, nompow, avg_fuelcons, propnumber, altitude, aspectratio, cx0, area, vmin, vmax, efficiency, fuelmass, aero_input)
breguet3_velocity = breguet3[0]
breguet3_times = breguet3[1]
breguet3_ranges = breguet3[2]

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

latex_breguet1_ranges = np.around(breguet1_ranges, decimals=3)
latex_breguet2_ranges = np.around(breguet2_ranges[::-1], decimals=3)
latex_breguet3_ranges = np.around(breguet3_ranges[::-1], decimals=3)
latex_breguet1_times = np.around(breguet1_times, decimals=3)
latex_breguet2_times = np.around(breguet2_times[::-1], decimals=3)
latex_breguet3_times = np.around(breguet3_times[::-1], decimals=3)

# print(len(latex_breguet1_ranges), len(latex_breguet2_ranges), len(latex_breguet1_times), len(latex_breguet2_times))

raw_data2 = {'Range V-H [km]': latex_breguet1_ranges[0::2],
            'Range alpha-H [km]': latex_breguet2_ranges[0::2],
            'Range V-alpha [km]': latex_breguet3_ranges[0::2],
            'Endurance V-H [100h]': latex_breguet1_times[0::2],
            'Endurance alpha-H [100h]': latex_breguet2_times[0::2],
            'Endurance V-alpha [100h]': latex_breguet3_times[0::2]
            }

df2 = pd.DataFrame(raw_data2, columns=['Range V-H [km]', 'Range alpha-H [km]', 'Range V-alpha [km]', 'Endurance V-H [100h]', 'Endurance alpha-H [100h]', 'Endurance V-alpha [100h]'])
df2.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/results-range-endurance-hawker.csv')

plt.show()