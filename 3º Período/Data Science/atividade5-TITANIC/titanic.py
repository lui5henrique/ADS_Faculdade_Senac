# ============================
# Análise de Dados - Titanic
# ============================
'''
Membros da equipe:
    Luis Henrique da Silva Araújo
    Rayza Dias Alves
    Ayrton Oliveira
    Pedro Leal
    Leticia Mendes
    Marcos Paraguaio
    Gilberto Quintino
    Nicolas Nobre
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns


# 1
# Importação da base de dados (dataset)
tabela_test = pd.read_csv('test.csv') #não será utilizada no projeto
#print(tabela_test)

# Importação da base de dados (dataset)
tabela_train = pd.read_csv('train.csv')
#print(tabela_train)

# 2. Padronizar as colunas
tabela_train.columns = [col.lower().replace(" ", "_") for col in tabela_train.columns]
# lower() para deixar todas as letras minúsculas
# replace(" ", "_") para substituir espaços por underline

# 3.  Remover colunas duplicadas
tabela_train.drop_duplicates(inplace=True) # Remover linhas duplicadas

# 4. Remover colunas vazias
tabela_train.dropna(how='all', axis=1, inplace=True)
# how='all' remove colunas que estão completamente vazias
# how='any' remove colunas que possuem pelo menos um valor vazio
# axis=1 para colunas
# axis=0 para linhas
# inplace=True para modificar o DataFrame original

# 5. Tratando tipos de dados
tabela_train['age'] = pd.to_numeric(tabela_train['age'], errors='coerce')
tabela_train['cabin'] = tabela_train['cabin'].astype(str)
tabela_train["sex"] = tabela_train["sex"].astype(str)
tabela_train["embarked"] = tabela_train["embarked"].astype(str)
tabela_train['fare'] = pd.to_numeric(tabela_train['fare'], errors='coerce')
tabela_train['survived'] = tabela_train['survived'].astype(str)
# errors='coerce' para forçar/converter valores inválidos em NaN
# astype(str) para converter para string

# 6. Linhas com valores vazios
tabela_train['age'].fillna(tabela_train['age'].median(), inplace=True)
tabela_train['cabin'].fillna(0)
tabela_train['embarked'].fillna('S', inplace=True)
tabela_train['fare'].fillna(tabela_train['fare'].median(), inplace=True)
# fillna() para preencher valores vazios
# median() para preencher com a mediana calculada da coluna
# inplace=True para modificar o DataFrame original

# 7. Padronizar valores de texto
tabela_train['survived'] = tabela_train['survived'].map({'0': 'Não', '1': 'Sim'})
tabela_train['embarked'] = tabela_train['embarked'].map({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
# map() para mapear valores específicos para novos valores (neste caso, nomes dos portos/cidades)

# 8. Criar colunas auxiliares (não é necessário nesta análise)

# mostrar o dataframe tratado
print(tabela_train)
print(tabela_train.info())

# Histograma da idade e sexo dos passageiros
plt.figure(figsize=(10, 6)) # Tamanho da figura
sns.histplot(data=tabela_train, x='age', hue='sex', bins=20, element='step') # Histograma com seaborn
plt.xlabel('Idade') # Rótulo do eixo x
plt.ylabel('Contagem') # Rótulo do eixo y
plt.title('Distribuição de Idade e por Sexo dos Passageiros do Titanic') # Título do gráfico
plt.grid(axis='y', alpha=0.75) # Adicionar grade no eixo y
plt.show()

# Gráfico de Pizza da Sobrevivência por Classe
survival_by_class = tabela_train.groupby('sex')['survived'].mean() # Calcular a taxa de sobrevivência por classe
plt.figure(figsize=(8, 8)) # Tamanho da figura
plt.pie(survival_by_class, labels=survival_by_class.index, autopct='%1.1f%%', startangle=140) # Gráfico de pizza
plt.axis('equal') # Garantir que o gráfico seja um círculo
plt.title('Taxa de Sobrevivência por Classe no Titanic') # Título do gráfico
plt.show()
