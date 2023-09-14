from sense_hat import SenseHat
from time import sleep
import numpy as np
import matplotlib.pyplot as plt


sense=SenseHat()
blue= (0,0,255)
yellow= (255,255,0)
red=(255,0,0)
q = 0
normal = []
avged = []
temperature_readings = []
averaged_readings = []
for x in range(0,10):
    
    temperature=sense.get_temperature()
    q += temperature
    temperature_readings.append(temperature)
    
    r = str(temperature)
    r = r[0:5]
    print(r)
    sleep(1)
q/=10
print(temperature_readings)




N = 10






for i in range(len(temperature_readings)):
    averaged_value = np.mean(temperature_readings[0:i+1])

        
    
    averaged_readings.append(averaged_value)
print(averaged_readings)


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
