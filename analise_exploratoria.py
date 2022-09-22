from turtle import title
import pandas as pd
import matplotlib.pyplot as plt

# leitura do arquivo
df = pd.read_csv('vgsales.csv')

'''
obs: sales - vendas nos valores de milhoes
'''


# remover valores faltantes
df.dropna(how='all', inplace=True)


# print(df.head())

# checar a margem de anos da base de dados.
# print(df['Year'].min())
# print(df['Year'].max())

# print(df.dtypes)


'''---------------------------------Gráficos--------------------------------------'''
# Agrupando por genêro e vendas seu totais globais, do ano de 1980 até 2020
# e mostrando em gráfico.
df_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
# print(df_genre.head())
df_genre.plot.bar(title='Genêro X Vendas Total Golbal em Milhões')


# Gráfico
# publisher e suas vendas globais do ano 1980 até 2020. Valores em milhões.
# somente os 15 primeiros pois não daria para visualizar corretamente
df_autora_mais_vendida = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
df_autora_mais_vendida = df_autora_mais_vendida.head(15)
df_autora_mais_vendida.plot.pie(title='Publishe X Vendas Globais')


# Grafico do agrupamento da publisher e suas vendas globais Anuais,
# em ordem das maiores vendas para as menores.
# somente os 20 primeiros pois não daria para visualizar corretamente todos.
df_autora_ano = df.groupby(['Publisher', 'Year'])['Global_Sales'].sum().sort_values(ascending=False)
df_autora_ano = df_autora_ano.head(20)
df_autora_ano.plot.bar(title='Publishe/Year X Vendas Globais')

# Gráfico
df_ano_venda = df.groupby('Year')['Global_Sales'].sum().sort_values(ascending=False)
# print(df_ano_venda.head())
df_ano_venda.plot.bar(title='Vendas X Ano')


'''---------------------- Meus arquivos das analises feitas -------------------'''

df_autora_mais_vendida = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
df_autora_ano = df.groupby(['Publisher', 'Year'])['Global_Sales'].sum().sort_values(ascending=False)


df_autora_mais_vendida.to_csv('Publicadora-mais-vendida.csv', index=False)
df_autora_ano.to_csv('Receita-Anual_Publicadora.csv')
