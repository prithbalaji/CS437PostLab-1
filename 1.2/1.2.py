import numpy as np
import matplotlib.pyplot as plt

N = 5

temperature_readings = [25.3, 25.4, 25.1, 25.8, 26.2, 25.7, 26.0, 25.9, 25.5, 25.4]


averaged_readings = []


for i in range(len(temperature_readings)):
    if i < N:
      
        averaged_value = temperature_readings[i]
    else:

        averaged_value = np.mean(temperature_readings[i - N : i + 1])
    
    averaged_readings.append(averaged_value)


time = np.arange(len(temperature_readings))


plt.figure(figsize=(10, 5))
plt.plot(time, temperature_readings, label='Original Readings', marker='o')
plt.plot(time, averaged_readings, label=f'Averaged (N={N})', marker='x')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Readings vs. Time')
plt.legend()
plt.grid(True)


plt.show()

