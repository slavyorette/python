import matplotlib.pyplot as plt
import numpy as np 

#Yield Values Recorded in Previous Studies of Urban Agriculture systems
#Robert McDougall, Paul Kristiansen and Romina Rader, 2019

data = {'tomatoes': [4.8,10.17], 
'fruit + veg': 2.34, 'mixed veg': [16.9,18.9],
'lettuce':39.9,}

tom_avg = np.mean(data['tomatoes'])
veg_avg = np.mean(data['mixed veg'])

x = data.keys()
crop_yield = [tom_avg, data['fruit + veg'], veg_avg,
data['lettuce']]

plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(x)] 

plt.bar(x_pos, crop_yield, color='purple')
plt.xlabel("Crop Type")
plt.ylabel("Yield (kg m-2 year -1 )")
plt.title("Yield from Urban Agriculture")
plt.xticks(x_pos, x)

plt.show()
