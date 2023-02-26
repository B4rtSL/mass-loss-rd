import pandas as pd
import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt

# 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx' 
foo = basf.aero_prep()

cz_arr = foo[1]
alph_arr = foo[0]
cx_arr = basf.cx(foo, 0.025, 4.41)
lift_drag = basf.lift_to_drag(cz_arr, cx_arr)

a = [2, 4, 6]
b = [2, 2, 2]
c = [a, b]
for i in c:
    print(c[0][i])
   
fig = plt.figure()
plt.plot(foo[0],lift_drag)
plt.show()