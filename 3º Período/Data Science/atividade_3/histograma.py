import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mydata.csv')
print(df['home_yellow'])

plt.hist(df['home_yellow'], bins=range(df['home_yellow'].min(), df['home_yellow'].max() + 2), color = 'yellow', edgecolor = 'gray')
plt.title('Histograma - Cartões Amarelos Time da Casa')
plt.xlabel('Número de Cartões Amarelos')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.25)

plt.show()