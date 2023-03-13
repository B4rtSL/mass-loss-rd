import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt

engine_prep = basf.engine_prep()
velocity = engine_prep[0]
eta = engine_prep[1]
disp_pow = engine_prep[2]
#disp_pow = np.multiply(1.3, disp_pow)
disp_pow_coeff = np.polyfit(velocity, disp_pow, 6)
eta_coeff = np.polyfit(velocity, eta, 6)

rpm_prep = basf.rpm_prep()
rpm = rpm_prep[0]
rpm_power = rpm_prep[1]
power_coeff6 = np.polyfit(rpm, rpm_power, 6)

new_velo_range = np.linspace(35, 200, 50)
new_rpm_range = np.linspace(0, 4000, 50)

pows_of_v = []
for i in new_velo_range:
    pow_of_v = 0
    pow_of_v = np.polyval(disp_pow_coeff, i)
    pows_of_v.append(pow_of_v)
powV_arr = np.array(pows_of_v)

powers6 = []
for i in new_rpm_range:
    new_power6 = np.polyval(power_coeff6, i)
    powers6.append(new_power6)
power_arr6 = np.array(powers6)

"""
def mixer(coeff_array1, deg, arg):
    right_arr = [0]*(deg+1)
    right_arr[deg] = right_arr[deg] + arg
    eq_arr = np.subtract(coeff_array1, right_arr)
    roots = np.roots(eq_arr)
    real_valued = roots.real[abs(roots.imag)<1e-5]
    for i in real_valued:
        if i>0 and np.polyval(coeff_array1, i) < arg + 0.1 and np.polyval(coeff_array1, i) > arg - 0.1:
            n = i
        else:
            n = 0
    return n
"""
pairs = []
for iter in powV_arr:
    pair = 0
    pair = basf.mixer(power_coeff6, 6, iter)
    pairs.append(pair)
rpm_of_velo_arr = np.array(pairs)

#print(rpm_of_velo_arr)

fuelcons = basf.fuelcons_prep()
rpm_fuelcons = fuelcons[0]
fuelcons_of_rpm = fuelcons[1]
fuelcons_coeff = np.polyfit(rpm_fuelcons, fuelcons_of_rpm, 6)
list_fuelcons = []
for iter3 in new_rpm_range:
    new_fuelcon = np.polyval(fuelcons_coeff, iter3)
    list_fuelcons.append(new_fuelcon)
fuelcons_arr = np.array(list_fuelcons)

list_new =[]
for iter4 in rpm_of_velo_arr:
    new = np.polyval(fuelcons_coeff, iter4)
    list_new.append(new)
fuel_of_V = np.array(list_new)
fuel_of_V_coeff = np.polyfit(new_velo_range, fuel_of_V, 6)


fig = plt.figure()
plt.plot(new_velo_range, rpm_of_velo_arr)
plt.xlabel("Velocity [m/s]")
plt.ylabel("RPM")
plt.title("RPM on Velocity")
fig2 = plt.figure()
plt.plot(new_velo_range, fuel_of_V)
plt.xlabel("Velocity [m/s]")
plt.ylabel("Specific Fuel Consumption [kg/kWh]")
plt.title("Specific Fuel Consumption on Velocity")
fig3 = plt.figure()
plt.plot(new_velo_range, powV_arr)
plt.xlabel("Velocity [m/s]")
plt.ylabel("Available Power [kW]")
plt.title("Available Power on Velocity")
fig4 = plt.figure()
plt.plot(rpm_fuelcons, fuelcons_of_rpm, 'o')
plt.xlabel("RPM")
plt.ylabel("Specific Fuel Consumption [kg/kWh]")
plt.title("Specific Fuel Consumption on RPM")
plt.show()