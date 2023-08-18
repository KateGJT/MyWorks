import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False
index = ['0~0.5', '0.6~2.0', '2.1~4.0', '4.1~6.0']
columns = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
np.random.seed(0)
data = pd.DataFrame(np.random.randint(30, 300, (4, 16)), index = index, columns = columns)
N = 16
theta = np.linspace(0, 2 * np.pi, N, endpoint = False)
width = np.pi / N 
labels = list(data.columns) 
plt.figure(figsize = (6, 6))
ax = plt.subplot(1, 1, 1, projection = 'polar')
for i in data.index:
    radius = data.loc[i] 
    ax.bar(theta, radius, width = width, bottom = 0.0, label = i, tick_label = labels)
ax.set_theta_zero_location('N') 
ax.set_theta_direction(-1)    
plt.title('各方向风速频数玫瑰图', fontsize = 20)
plt.legend(loc = 4, bbox_to_anchor = (1.3, 0.2)) 
plt.show()
