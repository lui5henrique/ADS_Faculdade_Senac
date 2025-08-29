
import pandas as pd           # Para manipulação do dataset
import matplotlib.pyplot as plt  # Para criação dos gráficos


# 1. Carregar o dataset
caminho = "mydata.csv"        # Caminho do arquivo CSV
df = pd.read_csv(caminho)     # Lê o arquivo e cria um DataFrame (tabela)


# 2. Selecionar a coluna de interesse
dados = df["home_yellow"]


# 3. Criar o Boxplot SEM mostrar outliers
plt.figure(figsize=(6, 4))                  # Define tamanho do gráfico
plt.boxplot(dados, showfliers=False)        # "showfliers=False" esconde os pontos outliers
plt.title("Boxplot - Home Yellow (sem outliers)")  # Título do gráfico
plt.ylabel("Cartões amarelos")              # Rótulo do eixo Y
plt.grid(True, linestyle="--", alpha=0.6)   # Adiciona grade para facilitar a leitura
plt.show()                                  # Exibe o gráfico
