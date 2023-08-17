import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('产品销售统计.xlsx')
n = data['产品名称']
x = data['销售量(件)']
y = data['销售额(元)']
z = data['毛利率(%)']
plt.scatter(x, y, s=z * 300, color='r', marker='o')
plt.xlabel('销售量(件)', fontdict={'family': 'Microsoft YaHei', 'color': 'k', 'size': 20}, labelpad=20)
plt.ylabel('销售额(元)', fontdict={'family': 'Microsoft YaHei', 'color': 'k', 'size': 20}, labelpad=20)
plt.title('销售量、销售额与毛利率关系图', fontdict={'family': 'Microsoft YaHei', 'color': 'k', 'size': 30}, loc='center')
for a, b, c in zip(x, y, n):
    plt.text(x=a, y=b, s=c, ha='center', va='center', fontsize=15, color='w')
plt.xlim(50, 600)
plt.ylim(2900, 11000)
plt.show()

