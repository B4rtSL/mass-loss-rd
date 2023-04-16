from advanced_alg import advanced_alg
from data_container import Cessna150

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"


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

