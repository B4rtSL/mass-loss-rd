import pandas as pd
import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt

# 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx' 
foo = basf.aero_prep()

cz_arr = foo[1]
alph_arr = foo[0]
cx_arr = basf.cx_arr(foo, 0.025, 4.41)
lift_drag = basf.lift_to_drag(cz_arr, cx_arr)

root = basf.poly_root(foo[0], foo[1], 5, basf.cz(2200, 1.225, 17, 150)) 
print(root)

coeff_arr = np.polyfit(foo[0], foo[1], 5)
new_alph_arr = np.linspace(root, max(alph_arr), 40)

czs = []
for i in new_alph_arr:
    new_cz = np.polyval(coeff_arr, i)
    czs.append(new_cz)

new_cz_arr = np.array(czs)
print(new_cz_arr)
fig = plt.figure()
plt.plot(foo[0],foo[1], new_alph_arr, new_cz_arr)
plt.show()