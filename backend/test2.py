import numpy as np
import basic_funcs as basf
import matplotlib.pyplot as plt
from data_container import Cessna150

aero_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"

aero_prep = basf.aero_prep(aero_input)

altitude = 2500
efficiency = 0.8
area = Cessna150.area
aspectratio = Cessna150.aspectratio
cx0 = Cessna150.cx0
avg_fuelcons = Cessna150.fuelcons
nompow = Cessna150.nompow
propnumber = Cessna150.propnumber
proptype = 'propeller'
startmass = Cessna150.startmass
vmax = Cessna150.vmax
vmin = Cessna150.vmin
fuelmass = Cessna150.fuelmass
air_density=1.2255*(1-(altitude/44300))**4.256

double_arr = basf.aero_prep(aero_input)
alpha_arr = double_arr[0]
cz_arr = double_arr[1]
alpha_root = basf.poly_root(alpha_arr, cz_arr, 5, basf.cz(704.682812501, air_density, area, vmax))
coeff_arr = np.polyfit(alpha_arr, cz_arr, 6)
new_alph_arr = basf.new_alph_arr(alpha_arr, alpha_root)
new_cz_arr = basf.new_cz_arr(new_alph_arr, coeff_arr)
new_cx_arr = basf.cx_arr(new_cz_arr, cx0, aspectratio)
lift_drag = basf.lift_to_drag(new_cz_arr, new_cx_arr)

print('cz og', cz_arr)
print('alpha og', alpha_arr)
print('cz new', new_cz_arr)
print('alpha new', new_alph_arr)