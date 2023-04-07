import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt
from data_container import Cessna150
import time
import math
start_time = time.time()


cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
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
power_disp_og = engine_prep[1]
velo_load = engine_prep[2]
power_load = engine_prep[3]

eta_velo = eta_prep[0]
eta = eta_prep[1]

new_rpm_range = np.linspace(min(fuel_rpm), max(fuel_rpm), 50)
new_velo_range = np.linspace(0, 100, 50)
new_eff_pow_range = np.linspace(min(rpm_power), max(rpm_power), 50)

power_load_arr = basf.new_values_array(velo_load, power_load, 1, new_velo_range)
power_disp = basf.new_values_array(velocity_power_disp, power_disp_og, 4, new_velo_range)

result = basf.poly_equation(velocity_power_disp, power_disp_og, 4, velo_load, power_load, 1)
print('Velo:', result)

power_arr6 = basf.new_values_array(rpm, rpm_power, 6, new_rpm_range)
fuelcons_arr = basf.new_values_array(fuel_rpm, fuelcons, 6, new_rpm_range)
eta_arr = basf.new_values_array(eta_velo, eta, 6, new_velo_range)

m_i = Cessna150.startmass
area = Cessna150.area
aspectratio = Cessna150.aspectratio
cx0 = Cessna150.cx0
range_step = 100
velocity = 56
time_step = range_step / velocity
fuelmass = Cessna150.fuelmass
end_mass = m_i - fuelmass + 14

eta_coeff = np.polyfit(eta_velo, eta, 6)
eta_of_chosen_velocity = np.polyval(eta_coeff, velocity)
fuel_of_power_coeff = np.polyfit(new_velo_range, fuelcons_arr, 6)
efficiency = eta_of_chosen_velocity
fig1 = plt.figure(0)
plt.plot(power_arr6, fuelcons_arr, '-k', )
plt.grid(which='both', axis='both')
plt.xlabel("Effective Power [kW]")
plt.ylabel("Specific Fuel Consumption [kg/kWh]")
plt.title("Specific Fuel Consumption versus Effective Power diagram")
plt.minorticks_on()

current_mass = Cessna150.startmass
i=0
essential_pow_list = []
effective_pow_list = []
fuelcons_list = []
iteration_list = []
endurances = []
ranges = []
while current_mass >= end_mass:
    i+=1
    iteration_list.append(i)
    essential_pow = current_mass*9.81*velocity/(basf.cz(current_mass, 1.225, area, velocity)/basf.cx(basf.cz(current_mass, 1.225, area, velocity), cx0, aspectratio))/1000
    essential_pow_list.append(essential_pow)
    effective_pow = essential_pow/eta_of_chosen_velocity
    if effective_pow > 75:
        effective_pow = 75
    effective_pow_list.append(effective_pow)
    #print('Effective', effective_pow)
    if effective_pow <= 75 and effective_pow >= 28:
        fuelcons_of_velo = np.polyval(fuel_of_power_coeff, effective_pow)
        fuelcons_list.append(fuelcons_of_velo)
        burnt_mass = time_step/3600*fuelcons_of_velo*effective_pow
        m_ii = current_mass - burnt_mass
        m_calc = (current_mass + m_ii)/2
    else:
        print('Power Values Exceeded')
        break


    A_factor=1.225*area*velocity*velocity*math.sqrt(cx0*3.14*aspectratio)
    endurance=1000*(efficiency/9.81/velocity/fuelcons_of_velo)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*current_mass/A_factor)-math.atan(2*9.81*m_ii/A_factor))
    range=3.6*velocity*endurance
    endurances.append(endurance)
    ranges.append(range)
    #essential_pow_corrected = m_calc*9.81*velocity/(basf.cz(m_calc, 1.225, area, velocity)/basf.cx(basf.cz(m_calc, 1.225, area, velocity), cx0, aspectratio))/1000
    #effective_pow_corrected = essential_pow_corrected/eta_of_chosen_velocity
    #print('Effective Corrected', effective_pow_corrected)
    #if effective_pow_corrected < 75 and effective_pow_corrected > 38:
        #fuelcons_of_velo_corrected = np.polyval(fuel_of_power_coeff, effective_pow_corrected)
        #burnt_mass_corrected = time_step/3600*fuelcons_of_velo_corrected*effective_pow_corrected
        #m_ii_corrected = m_i - burnt_mass_corrected
    #else:
    #    break

    current_mass = m_ii
    #print('Current mass is', current_mass)
    
    #print('Counter:', i)

print('efficiency:', efficiency)
print('Expected endmass is:', end_mass)
print('Final mass is:', current_mass)
print('Range iterated is:', i*range_step/1000, 'km')

#print('Essential pow list:',essential_pow_list)

essential_pow_array = np.array(essential_pow_list)
effective_pow_array = np.array(effective_pow_list)
fuelcons_of_velo_array = np.array(fuelcons_list)
velocity_array_pom = [1] * len(essential_pow_array)
iteration_array = np.array(iteration_list)
velocity_array = np.multiply(velocity_array_pom, velocity)
range_array = np.array(ranges)
range_result = np.sum(range_array)

print('Range result', range_result)
plt.figure(1)
plt.subplot(311)
plt.plot(iteration_array, essential_pow_array, '-')
plt.title("Essential Power")
plt.subplot(312)
plt.plot(iteration_array, effective_pow_array, '-')
plt.title("Effective Power")
plt.subplot(313)
plt.plot(iteration_array, fuelcons_of_velo_array, '-')
plt.title("Fuelcons")

plt.figure(2)
plt.plot(new_rpm_range, power_arr6, 'k-')
plt.title("Effective Power on RPM")
plt.grid(which='both', axis='both')
plt.minorticks_on()
plt.show()






#print("--- %s seconds ---" % (time.time() - start_time))