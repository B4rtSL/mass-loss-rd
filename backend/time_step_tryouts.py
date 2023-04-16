from advanced_alg import advanced_alg
from data_container import Cessna150

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"


results1, time1 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 1)
print('Krok 1s:', time1)

results5, time5 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 5)
print('Krok 5s:', time5)

results10, time10 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 10)
print('Krok 10s:', time10)

results30, time30 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 30)
print('Krok 30s:', time30)


results60, time60 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 60)
print('Krok 60s:', time60)