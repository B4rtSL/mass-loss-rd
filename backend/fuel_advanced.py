import pandas as pd
import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt

engine_prep = basf.engine_prep()

velocity = engine_prep[0]
eta = engine_prep[1]
disp_pow = engine_prep[2]

'''
eff_pow = np.divide(disp_pow, eta)
print(disp_pow)
print(eta)
print(eff_pow)
'''

eta_coeff = np.polyfit(velocity, eta, 6)
disp_pow_coeff = np.polyfit(velocity, disp_pow, 6)

new_velo_range = np.linspace(0, 200, 50)
new_rpm_range = np.linspace(0, 4000, 50)

'''
i_s =[]
for i in new_velo_range:
    new_i = i**2+2
    i_s.append(new_i)
i_arr = np.array(i_s)
'''

etas = []
for i in new_velo_range:
    new_eta = np.polyval(eta_coeff, i)
    etas.append(new_eta)
eta_arr = np.array(etas)

disp_pows = []
for i in new_velo_range:
    new_disp_pow = np.polyval(disp_pow_coeff, i)
    disp_pows.append(new_disp_pow)
disp_pow_arr = np.array(disp_pows)

rpm_prep = basf.rpm_prep()
rpm = rpm_prep[0]
rpm_power = rpm_prep[1]

'''
power_coeff5 = np.polyfit(rpm, rpm_power, 5)
powers5 = []
for i in new_rpm_range:
    new_power5 = np.polyval(power_coeff5, i)
    powers5.append(new_power5)
power_arr5 = np.array(powers5)
'''

#good enough fittment to attached dataset
power_coeff6 = np.polyfit(rpm, rpm_power, 6)
powers6 = []
for i in new_rpm_range:
    new_power6 = np.polyval(power_coeff6, i)
    powers6.append(new_power6)
power_arr6 = np.array(powers6)

"""
right_arr = [0]*(7)
right_arr[6] = right_arr[6] + 1500
eq_arr = np.subtract(power_coeff6, right_arr)
roots = np.roots(eq_arr)
real_valued = roots.real[abs(roots.imag)<1e-5]


for i in real_valued:
    pom = 0
    pom = i
    if pom>0:
        n = pom


second_right_arr = [0]*(7)
second_right_arr[6] = second_right_arr[6] + 1500
second_eq_arr = np.subtract(disp_pow_coeff, second_right_arr)
second_roots = np.roots(second_eq_arr)
second_real_valued = second_roots.real[abs(second_roots.imag)<1e-5]


for x in second_real_valued:
    pom2 = 0
    pom2 = x
    if pom2 > 0:
        y = pom2
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
    '''
    second_right_arr = [0]*(deg+1)
    second_right_arr[deg] = second_right_arr[deg] + arg
    second_eq_arr = np.subtract(coeff_array2, second_right_arr)
    second_roots = np.roots(second_eq_arr)
    second_real_valued = second_roots.real[abs(second_roots.imag)<1e-5]

    for x in second_real_valued:
        pom2 = 0
        pom2 = x
        if pom2 > 0:
            v = pom2
    '''

    return n

#print(mixer(power_coeff6, disp_pow_coeff, 6, 1500))

new_power_range = np.linspace(150, 2000, 50)
pairs = []
for iter in new_power_range:
    pair = 0
    pair = mixer(power_coeff6, 6, iter)
    pairs.append(pair)

pairs2 = []
for iter2 in new_power_range:
    pair2 = 0
    pair2 = mixer(disp_pow_coeff, 6, iter2)
    pairs2.append(pair2)

rpm_of_velo_arr = np.array(pairs)
velo_for_rpm_arr = np.array(pairs2)

#print(disp_pow)
#fig = plt.figure()
#plt.plot(rpm, rpm_power, 'o', new_rpm_range, power_arr6)


fig2 = plt.figure()
plt.plot(velo_for_rpm_arr, rpm_of_velo_arr, 'o')
plt.show()