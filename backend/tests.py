import pandas as pd
import numpy as np
from scipy import interpolate
import basic_funcs
import matplotlib.pyplot as plt

# 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx'
test2 = input()

def aero_prep(path):
    data = pd.read_excel(path)
    #print(data)

    # considering 2 column file with alpha (deg) angle in 1st column and Cz in 2nd
    list_cz = data['cz-plane'].values.tolist()
    array_cz = np.array(list_cz)

    list_alpha = data['alpha-plane'].values.tolist()
    array_alpha = np.array(list_alpha)

    # 1st column - alpha degree, 2nd column cz coeff.
    double_arr = [array_alpha, array_cz]

    return double_arr
    #interpolation of cz(alpha)
    f = interpolate.interp1d(array_alpha, array_cz)
    
    x_max = max(array_alpha)
    x_min = min(array_alpha)
    xnew = np.arange(x_min, x_max, 1)
    ynew = f(xnew)
    
  
foo = aero_prep(test2)

cz_arr = foo[1]
alph_arr = foo[0]
print(max(cz_arr))
print(min(cz_arr))
print(len(cz_arr))

for i in range(len(cz_arr)):
    if cz_arr[i] == max(cz_arr):
        max_value_index = i

for j in range(len(cz_arr)):
    if cz_arr[j] == min(cz_arr):
        min_value_index = j

print(max_value_index)
print(min_value_index)
new_cz_arr = cz_arr[min_value_index:max_value_index+1]
print(new_cz_arr)
new_alpha_arr = alph_arr[min_value_index:max_value_index+1]

coeff_arr = np.polyfit(new_alpha_arr, new_cz_arr,5)
reverse_coeff_arr = coeff_arr[::-1]
#print(coeff_arr)
#print(reverse_coeff_arr)
polies = []
"""
for i in new_alpha_arr:
    poly = i**0*reverse_coeff_arr[0] + i**1*reverse_coeff_arr[1] + i**2*reverse_coeff_arr[2] + i**3*reverse_coeff_arr[3] + i**4*reverse_coeff_arr[4] + i**5*reverse_coeff_arr[5] 
    polies.append(poly)
polies_arr=np.array(polies)
"""

for i in new_alpha_arr:
    pom = 0
    poly = 0
    for j in range(6):
        pom = reverse_coeff_arr[j]*i**j
        poly = poly + pom 
    polies.append(poly)
polies_arr=np.array(polies)
print(polies_arr)

fig = plt.figure()
plt.plot(foo[0],foo[1], new_alpha_arr, polies_arr, new_alpha_arr, new_cz_arr)
plt.show()