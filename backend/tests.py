import pandas as pd
import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt
from data_container import Cessna150
import time
start_time = time.time()


cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
foo = basf.aero_prep(cz_input)

cz_arr = foo[1]
alph_arr = foo[0]
cx_arr = basf.cx_arr(foo, 0.025, 4.41)
lift_drag = basf.lift_to_drag(cz_arr, cx_arr)

root = basf.poly_root(foo[0], foo[1], 5, basf.cz(2200, 1.225, 17, 150)) 

coeff_arr = np.polyfit(foo[0], foo[1], 5)
new_alph_arr = np.linspace(root, max(alph_arr), 40)

czs = []
for i in new_alph_arr:
    new_cz = np.polyval(coeff_arr, i)
    czs.append(new_cz)
new_cz_arr = np.array(czs)


fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

rpm_prep = basf.rpm_prep(rpm_input_cessna)
fuelcons_prep = basf.fuelcons_prep(fuelcons_input_cessna)
engine_prep = basf.engine_prep_const_blade(engine_input)
eta_prep = basf.eta_prep(eta_input)

rpm = rpm_prep[0]
rpm_power = rpm_prep[1]

fuel_rpm = fuelcons_prep[0]
fuelcons = fuelcons_prep[1]

velocity_power_disp = engine_prep[0]
power_disp = engine_prep[1]
velo_load = engine_prep[2]
power_load = engine_prep[3]

eta_velo = eta_prep[0]
eta = eta_prep[1]

new_rpm_range = np.linspace(2000, 3000, 50)
new_velo_range = np.linspace(0, 100, 50)


power_load_arr = np.divide(basf.new_values_array(velo_load, power_load, 1, new_velo_range), 1000)
power_disp = np.divide(basf.new_values_array(velocity_power_disp, power_disp, 4, new_velo_range), 1000)
power_arr6 = basf.new_values_array(rpm, rpm_power, 6, new_rpm_range)
fuelcons_arr = basf.new_values_array(fuel_rpm, fuelcons, 6, new_rpm_range)
eta_arr = basf.new_values_array(eta_velo, eta, 6, new_velo_range)

m_i = Cessna150.startmass
area = Cessna150.area
aspectratio = Cessna150.aspectratio
cx0 = Cessna150.cx0
range_step = 1000
velocity = 58
time_step = range_step / velocity

essential_pow = m_i*9.81*velocity/(basf.cz(m_i, 1.225, area, velocity)/basf.cx(basf.cz(m_i, 1.225, area, velocity), cx0, aspectratio))/1000
print('Essential pow is:', essential_pow)

eta_coeff = np.polyfit(eta_velo, eta, 6)
eta_of_chosen_velocity = np.polyval(eta_coeff, velocity)
print('Eta is:', eta_of_chosen_velocity)

effective_pow = essential_pow/eta_of_chosen_velocity
print('Effective pow is:', effective_pow)

fuel_of_power_coeff = np.polyfit(new_velo_range, fuelcons_arr, 6)
fuelcons_of_velo = np.polyval(fuel_of_power_coeff, effective_pow)

print('fuelcons is:', fuelcons_of_velo)

burnt_mass = time_step/3600*fuelcons_of_velo*effective_pow
print('Burnt mass is:', burnt_mass)

m_ii = m_i - burnt_mass
print('M_ii:',m_ii)

m_calc = (m_i + m_ii)/2

essential_pow_corrected = m_calc*9.81*velocity/(basf.cz(m_calc, 1.225, area, velocity)/basf.cx(basf.cz(m_calc, 1.225, area, velocity), cx0, aspectratio))/1000
print('Corrected essential power is:', essential_pow_corrected)

effective_pow_corrected = essential_pow_corrected/eta_of_chosen_velocity
print('Effective pow corrected is:', effective_pow_corrected)

fuelcons_of_velo_corrected = np.polyval(fuel_of_power_coeff, effective_pow_corrected)

burnt_mass_corrected = time_step/3600*fuelcons_of_velo_corrected*effective_pow_corrected

print(burnt_mass_corrected)

m_ii_corrected = m_i - burnt_mass_corrected

print('M_ii_corrected = mass after first step:',m_ii_corrected)

a1 = 10
current_a = a1
counter = 0
while current_a > 2:
    help_a = current_a * 0.1
    current_a = current_a - help_a
    counter += 1

print(counter)
print(current_a)







print("--- %s seconds ---" % (time.time() - start_time))

