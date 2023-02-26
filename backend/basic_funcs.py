import numpy as np
import pandas as pd
from scipy import interpolate

g=9.81
test = 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx'

def velocity(mass, rho, area, cz):
    velocity = (2*mass*g/rho/area/cz)**0.5
    return print(velocity)

#this function takes path to excel file with data as an agrument and returns the data in array of 2 1D arrays
def aero_prep(path):
    data = pd.read_excel(path)

    # considering 2 column file with alpha (deg) angle in 1st column and Cz in 2nd
    list_cz = data['cz-plane'].values.tolist()
    array_cz = np.array(list_cz)

    list_alpha = data['alpha-plane'].values.tolist()
    array_alpha = np.array(list_alpha)

    # 1st column - alpha degree, 2nd column cz coeff.
    double_arr = [array_alpha, array_cz]

    return double_arr

def interpolator(double_arr):
    coeff_arr = np.polyfit(double_arr[0], double_arr[1], 6)
    reverse_coeff_arr = coeff_arr[::-1]
    polies = []
    for i in double_arr[0]:
        for j in range(7):
            pom = i**j*reverse_coeff_arr[j]
            poly = poly + pom 
        polies.append(poly)
    polies_arr=np.array(polies)
    return print(polies_arr)


def cx(aero_prep, cx0, lambda_e):
    path = input()
    double_arr = aero_prep(path)
    cz = double_arr[1]
    pi=np.pi
    cx  = []
    for i in cz:
        cxs=cx0+i*i/pi/lambda_e
        cx.append(cxs)

    array_cx = np.array(cx)
    return array_cx

#def lift_to_drag(aero_prep, cx):