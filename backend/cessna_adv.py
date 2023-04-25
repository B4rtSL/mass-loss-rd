from advanced_alg import advanced_alg
from data_container import Cessna150
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cz_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-cz-data.xlsx"
fuelcons_input_cessna = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-fuelcons-load-data.xlsx"
rpm_input_cessna = 'C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-rpm-load-data.xlsx'
engine_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/cessna-power-const.xlsx"
eta_input = "C:/Users/barto/Desktop/inżynierka/test-data/cessna-data/eta-velo.xlsx"

results, time, cpu = advanced_alg(rpm_input_cessna, fuelcons_input_cessna, eta_input, Cessna150, 762, 30)

ranges = results[0]
endurances = np.multiply(100, results[1])
velocities = results[2]

print(ranges, endurances, velocities)
print(len(ranges), len(endurances), len(velocities))

fig4 = plt.figure()
plt.plot(velocities, ranges, label = "Range")
plt.plot(velocities, endurances, label = "Endurance")

plt.legend(loc="best")
plt.xlabel("Velocity [km/h]")
plt.ylabel("Endurance [100h] and Range [km]")
plt.title("Range and Endurance vs Velocity")
plt.grid(which='both', axis='both')
plt.show()