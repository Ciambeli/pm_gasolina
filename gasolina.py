# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_df

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico.set(title='Preço Médio da Gasolina', xlabel='Dias', ylabel='Preço (BRL)');

plt.savefig('gasolina.png')