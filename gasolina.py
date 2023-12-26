# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_df

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico.set(title='Preço dos 10 primeiros dias do mês.', xlabel='Days', ylabel='(BRL)');

plt.savefig('gasolina.png')
