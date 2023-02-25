import pandas as pd
import numpy as np
from scipy import interpolate

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
print(foo[1])
