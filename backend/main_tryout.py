from advanced_alg import advanced_alg
from data_container import Cessna150
import numpy as np
import pandas as pd

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

results05, time05, cpu05 = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 0, 15)
print('Krok 15s:', time05, 'CPU:', cpu05)