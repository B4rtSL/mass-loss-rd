import numpy as np
import pandas as pd
from scipy import interpolate

g=9.81
test = 'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx'

def velocity(mass, rho, area, cz):
    velocity = (2*mass*g/rho/area/cz)**0.5
    return velocity

def cz(mass, rho, area, V):
    cz = 2*mass*g/rho/area/V**2
    return cz

def velocity_arr(mass, rho, area, cz_arr):
    velocities = []
    for i in cz_arr:
        velocity = (2*mass*g/rho/area/i)**0.5
        velocities.append(velocity)
    velocity_arr = np.array(velocities)
    return velocity_arr

#this function takes path to excel file with data as an agrument and returns the data in array of 2 1D arrays
def aero_prep():
    data = pd.read_excel(r'C:/Users/barto/Desktop/inżynierka/test-data/cz-data.xlsx')

    # considering 2 column file with alpha (deg) angle in 1st column and Cz in 2nd
    list_cz = data['cz-plane'].values.tolist()
    array_cz = np.array(list_cz)

    list_alpha = data['alpha-plane'].values.tolist()
    array_alpha = np.array(list_alpha)

    #finding of max and min values indexes
    for i in range(len(array_cz)):
        if array_cz[i] == max(array_cz):
            max_value_index = i

    for j in range(len(array_cz)):
        if array_cz[j] == min(array_cz):
            min_value_index = j

    #cutting original input arrays to needed range of values for better fit
    new_cz_arr = array_cz[min_value_index:max_value_index+1]
    new_alpha_arr = array_alpha[min_value_index:max_value_index+1]

    # 1st column - alpha degree, 2nd column cz coeff.
    double_arr = [new_alpha_arr, new_cz_arr]

    return double_arr

#this function prepares drag-polar array based on cz-charasteristics and user input
def cx_arr(aero_prep_res, cx0, lambda_e):
    double_arr = aero_prep_res
    cz = double_arr[1]
    pi=np.pi
    cx  = []
    for i in cz:
        cxs=cx0+i*i/pi/lambda_e
        cx.append(cxs)
    array_cx = np.array(cx)
    return array_cx

#non-array drag-polar
def cx(cz, cx0, lambda_e):
    pi=np.pi
    return cx0 + cz*cz/pi/lambda_e

#this function takes users input file consisting of cz/alpha points and returns array of interpolated values
#args are results of aero-prep and degree of wanted polynomial
def interpolator(double_arr, deg, new_arg_range_arr):
    coeff_arr = np.polyfit(double_arr[0], double_arr[1], deg)
    reverse_coeff_arr = coeff_arr[::-1]
    polies = []
    for i in new_arg_range_arr:
        pom = 0
        poly = 0
        for j in range(deg+1):
            pom = reverse_coeff_arr[j]*i**j
            poly = poly + pom 
        polies.append(poly)
    polies_arr=np.array(polies)
    return polies_arr

#this function returns lift-to-drag coeff
def lift_to_drag(cz, cx):
    array_cz = cz
    array_cx = cx
    lift_drag = np.divide(array_cz, array_cx)
    return lift_drag

#this function solves polynomial eq with known right side and returns real root within predicted range
#
def poly_root(x_es, y_es, deg, arg):
    coeff_arr = np.polyfit(x_es, y_es, deg)
    right_arr = [0] * (deg+1)
    right_arr[deg] = right_arr[deg] + arg
    eq_arr = np.subtract(coeff_arr, right_arr)
    roots = np.roots(eq_arr)
    real_valued = roots.real[abs(roots.imag)<1e-5]

    for i in real_valued:
        if np.polyval(coeff_arr, i) < arg + 1 and np.polyval(coeff_arr, i) > arg - 1:
         searched = i

    return searched
    
