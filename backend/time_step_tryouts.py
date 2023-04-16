from advanced_alg import advanced_alg
from data_container import Cessna150
import numpy as np
import pandas as pd

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

results05, time05, cpu05 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 0.5)
print('Krok 1s:', time05, 'CPU:', cpu05)

results1, time1, cpu1 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 1)
print('Krok 1s:', time1, 'CPU:', cpu1)

results5, time5, cpu5 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 5)
print('Krok 5s:', time5, 'CPU:', cpu5)

results10, time10, cpu10 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 10)
print('Krok 10s:', time10, 'CPU:', cpu10)

results15, time15, cpu15 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 15)
print('Krok 15s:', time15, 'CPU:', cpu15)

results30, time30, cpu30 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 30)
print('Krok 30s:', time30, 'CPU:', cpu30)

results60, time60, cpu60 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 60)
print('Krok 60s:', time60, 'CPU:', cpu60)

array_Wtimes = [time05, time1, time5, time10, time15, time30, time60]
array_CPUtimes = [cpu05, cpu1, cpu5, cpu10, cpu15, cpu30, cpu60]

latex_Wtimes = np.around(array_Wtimes, decimals=5)
latex_CPUtimes = np.around(array_CPUtimes, decimals=5)

raw_data = {'Wall time [s]': latex_Wtimes,
            'CPU time [s]': latex_CPUtimes
            }

df = pd.DataFrame(raw_data, columns=['Wall time [s]', 'CPU time [s]'])
df.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/results-time-step.csv')

array_range_results = [results05[0], results1[0], results5[0], results10[0], results15[0], results30[0], results60[0]]
array_endurance_results = [results05[1], results1[1], results5[1], results10[1], results15[1], results30[1], results60[1]]

error_list = []
for result in array_range_results:
    error = np.divide(abs(np.subtract(results05[0], result)), results05[0])
    error_list.append(error)

mpe_list = []
for array in error_list:
    summed = np.sum(array)
    mpe = 100 * summed / len(array)
    mpe_list.append(mpe)

latex_mpes = np.around(mpe_list, decimals=5)

mpes_data_raw = {'MPE [%]': latex_mpes} 
df2 = pd.DataFrame(mpes_data_raw, columns=['MPE [%]'])
df2.to_csv('C:/Users/barto/Desktop/inżynierka/test-data/test-results/results-mpe.csv')