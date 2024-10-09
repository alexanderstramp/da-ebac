# código de geração do gráfico 

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

# Lendo o arquivo csv
gasolina_df = pd.read_csv('gasolina.csv')

# gerando o grafico
grafico = sns.barplot(data=gasolina_df, x='dia', y='venda')

# salvando o grafico
plt.savefig('gasolina.png')