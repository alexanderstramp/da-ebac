# código de geração do gráfico

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo csv
gasolina_df = pd.read_csv('gasolina.csv')

# gerando o grafico
grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
grafico.set(title='Preço da Gasolina em SP', xlabel='Dias', ylabel='Preços')


# salvando o grafico
plt.savefig('gasolina.png')
