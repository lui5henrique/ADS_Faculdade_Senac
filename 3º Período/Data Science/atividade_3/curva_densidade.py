import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# 1. Carregar os dados
df = pd.read_csv("mydata.csv")  # Lê o CSV do diretório atual.
dados = df["home_yellow"].dropna().astype(float).values  # Seleciona a coluna, remove NaN, garante tipo float e vira array NumPy.

# 2. Criar o grid de valores para o eixo X
x_min, x_max = dados.min(), dados.max()   # Pega o valor mínimo e máximo da coluna
x_vals = np.linspace(x_min, x_max, 200)   # Cria 200 pontos entre min e max (suavidade do gráfico)

# 3. Calcular curva de densidade usando KDE
kde = gaussian_kde(dados)     # Cria o estimador de densidade baseado nos dados
densidade = kde(x_vals)       # Calcula a densidade para cada ponto do grid

# 4. Criar o gráfico
plt.figure(figsize=(8,5))  # Define o tamanho do gráfico (8x5 polegadas)

plt.plot(x_vals, densidade, color="gray", linewidth=2, label="Curva de Densidade")  
# Plota a curva KDE em azul, com linha mais grossa e rótulo para legenda

plt.fill_between(x_vals, densidade, alpha=0.2, color="yellow")  
# Preenche a área sob a curva para dar destaque visual

plt.title("Curva de Densidade - Home Yellow Cards")  # Título do gráfico
plt.xlabel("Número de Cartões Amarelos (time da casa)")  # Rótulo do eixo X
plt.ylabel("Densidade de probabilidade")  # Rótulo do eixo Y
plt.legend()  # Mostra a legenda
plt.grid(alpha=0.3)  # Adiciona uma grade leve para facilitar leitura
plt.show()  # Exibe o gráfico