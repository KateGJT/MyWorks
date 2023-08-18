import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False 
data = pd.read_excel('汽车性能指标分值统计表.xlsx')  
data = data.set_index('性能评价指标')  
data = data.T  
data.index.name = '品牌'  
def plot_radar(data, feature):  
    columns = ['动力性', '燃油经济性', '制动性', '操控稳定性', '行驶平顺性', '通过性', '安全性', '环保性', '方便性', '舒适性', '经济性', '容量性'] 
    colors = ['r', 'g', 'y']  
    angles = np.linspace(0.1 * np.pi, 2.1 * np.pi, len(columns), endpoint = False)  
    angles = np.concatenate((angles, [angles[0]]))    
    figure = plt.figure(figsize = (6, 6))  
    ax = figure.add_subplot(1, 1, 1, projection = 'polar')
    for i, c in enumerate(feature):
        stats = data.loc[c]  
        stats = np.concatenate((stats, [stats[0]]))  
        ax.plot(angles, stats, '-', linewidth = 2, c = colors[i], label = str(c))
        ax.fill(angles, stats, color = colors[i], alpha = 0.75)  
    ax.legend(loc = 4, bbox_to_anchor = (1.15, -0.07))  
    ax.set_yticklabels([2, 4, 6, 8, 10])  
    ax.set_thetagrids(angles * 180 / np.pi, columns, fontsize = 12)  
    plt.show()
    return figure
figure = plot_radar(data, ['A品牌', 'B品牌', 'C品牌'])
figure = plot_radar(data, ['B品牌'])
