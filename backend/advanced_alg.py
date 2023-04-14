import math
import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt
from data_container import Cessna150
from data_container import airplane
import time

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

def advanced_alg(rpm_input, fuelcons_input, eta_input, airplane: object, altitude, time_step):
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
    m_i = airplane.startmass
    area = airplane.area
    aspectratio = airplane.aspectratio
    cx0 = airplane.cx0
    fuelmass = airplane.fuelmass
    wmax = airplane.wmax
    nompow = airplane.nompow
    avg_fuelcons = airplane.fuelcons
    propnumber = airplane.propnumber

    new_velo_range = np.linspace(vmin, vmax, 50)
    fuel_of_power_coeff = np.polyfit(new_velo_range, fuelcons_arr, 6)
    velocity_range = np.linspace(vmin, vmax, 50)
    eta_coeff = np.polyfit(eta_velo, eta, 6)

    air_density = 1.2255 * (1-(altitude/44300))**4.256
    
    print('Please type fuelmass calculating method\nAvailable methods are:\nRaymer\nPaturski\nAuthors')
    decision = input()

    if decision == 'Raymer':
        end_mass = m_i*0.995*0.988*0.997*0.995
    elif decision == 'Paturski':
        diffmass = propnumber*nompow*avg_fuelcons*0.75
        end_mass = m_i - fuelmass + diffmass
    elif decision == 'Authors':
        fuel_takeoff = avg_fuelcons * nompow / 3600 / wmax * (altitude)
        end_mass = m_i - fuelmass + fuel_takeoff + m_i*(1-0.995)
    print(end_mass, vmin, vmax)
    ranges_final_list = []
    essential_pow_list = []
    effective_pow_list = []
    start_time = time.time()
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
                print('Power Values Exceeded')
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


    ranges_final_array = np.array(ranges_final_list)
    velocity_range = np.multiply(velocity_range, 3.6)

    print("--- %s seconds ---" % (time.time() - start_time))
    return ranges_final_array


results = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 30)

print(results)

