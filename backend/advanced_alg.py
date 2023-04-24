import math
import numpy as np
import basic_funcs as basf
from data_container import Cessna150
import time

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

def advanced_alg(rpm_input, fuelcons_input, eta_input, airplane: object, altitude, time_step):
    cpu_start_time = time.process_time()
    
    print('Please type fuelmass calculating method\nAvailable methods are:\nRaymer\nPaturski\nAuthors')
    type_calc = basf.mass_calc_type(airplane, altitude)

    start_time = time.time()

    rpm_prep = basf.rpm_prep(rpm_input)
    rpm = rpm_prep[0]
    rpm_power = rpm_prep[1]
    new_rpm_range = np.linspace(min(rpm), max(rpm), 50)

    fuelcons_prep = basf.fuelcons_prep(fuelcons_input)
    fuel_rpm = fuelcons_prep[0]
    fuelcons = fuelcons_prep[1]
    
    eta_prep = basf.eta_prep(eta_input)
    eta_velo = eta_prep[0]
    eta = eta_prep[1]
    
    fuelcons_arr = basf.new_values_array(fuel_rpm, fuelcons, 6, new_rpm_range)
    
    #assignment of objects values to new arguments
    vmin = airplane.vmin
    vmax = airplane.vmax
    area = airplane.area
    aspectratio = airplane.aspectratio
    cx0 = airplane.cx0

    air_density = 1.2255 * (1-(altitude/44300))**4.256
    
    m_i = type_calc[0]
    end_mass = type_calc[1]
    ranges_final_list = []
    endurances_final_list = []
    essential_pow_list = []
    effective_pow_list = []

    vmin = basf.velocity(m_i, air_density, area, 1.15)
    new_velo_range = np.linspace(vmin, vmax, 50)
    fuel_of_power_coeff = np.polyfit(new_velo_range, fuelcons_arr, 6)
    velocity_range = np.linspace(vmin, vmax, 50)
    eta_coeff = np.polyfit(eta_velo, eta, 6)

    for velocity in velocity_range:
        ranges = []
        endurances = []
        eta_of_chosen_velocity = np.polyval(eta_coeff, velocity)
        efficiency = eta_of_chosen_velocity
        current_mass = m_i

        while current_mass >= end_mass:

            essential_pow = current_mass*9.81*velocity/(basf.cz(current_mass, air_density, area, velocity)/basf.cx(basf.cz(current_mass, air_density, area, velocity), cx0, aspectratio))/1000
            essential_pow_list.append(essential_pow)
            effective_pow = essential_pow/eta_of_chosen_velocity
            effective_pow_list.append(effective_pow)

            if effective_pow <= max(rpm_power) and effective_pow >= min(rpm_power):
                fuelcons_of_velo = np.polyval(fuel_of_power_coeff, effective_pow)
                burnt_mass = time_step/3600*fuelcons_of_velo*effective_pow
                m_ii = current_mass - burnt_mass
            else:
                effective_pow = airplane.nompow
                fuelcons_of_velo = np.polyval(fuel_of_power_coeff, effective_pow)
                burnt_mass = time_step/3600*fuelcons_of_velo*effective_pow
                m_ii = current_mass - burnt_mass
                print('Power Values Exceeded, Max Available Value Taken.')
                break

            A_factor=air_density*area*velocity*velocity*math.sqrt(cx0*3.14*aspectratio)
            endurance=1000*(efficiency/9.81/velocity/fuelcons_of_velo)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*current_mass/A_factor)-math.atan(2*9.81*m_ii/A_factor))
            range=3.6*velocity*endurance
            endurances.append(endurance)
            ranges.append(range)

            current_mass = m_ii
        
        range_array = np.array(ranges)
        range_result = np.sum(range_array)
        ranges_final_list.append(range_result)
        endurance_array = np.array(endurances)
        endurance_result = np.sum(endurance_array)
        endurances_final_list.append(endurance_result)

    ranges_final_array = np.array(ranges_final_list)
    endurances_final_array = np.array(endurances_final_list)
    velocity_range = np.multiply(velocity_range, 3.6)

    triple_array = [ranges_final_array, endurances_final_array, velocity_range]
    end_time = (time.time() - start_time)
    cpu_end_time = (time.process_time() - cpu_start_time)
    return triple_array, end_time, cpu_end_time
