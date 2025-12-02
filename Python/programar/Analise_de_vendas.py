
#importando a biblioteca pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#carregando o arquivo dos dados 
df = pd.read_csv("dados_venda_empresa1.csv.csv")

#mostrando as colunas dos dados de forma organizada
print (df.columns.tolist())

#verificando se tem dados faltando e somando eles em seguida com o SUM 

dados_faltantes = df.isnull().sum()

#mostrando os dados faltantes
print(dados_faltantes)

#resumo estatistico sobre todos os dados da nossa tabela !!
print (df.describe())

#valores zerados em colunas numericas
print(df[['quantidade','preco_unitario','total_venda']].eq(0).sum())

#operacoes basicas no pandas
#somando uma coluna com o metodo SUM
print(df[['total_venda']].sum())

#multiplicando colunas
#print(df['total_venda'] = df['quantidade'] * df['preco_unitario'])


#media de colunas da total venda
print(df['quantidade'].mean())

#media de quantidade vendida por categoria
print(df.groupby('categoria')['quantidade'].mean())

#soma de quantidade vendida por categoria
print(df.groupby('categoria')['quantidade'].sum())

#multiplas estatisticas por categoria
print(df.groupby('categoria')['quantidade'].agg(['mean', 'sum', 'count', 'max', 'min']))

df['preco_unitario'] = (
    df['preco_unitario']
    .astype(str)                            # garante que é string
    .str.replace('.', '', regex=False)     # remove ponto dos milhares
    .str.replace(',', '.', regex=False)    # troca vírgula decimal por ponto
)

# 2. Converter para float
df['preco_unitario'] = pd.to_numeric(df['preco_unitario'], errors='coerce')

# 3. Converter quantidade, se necessário
df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')

# 4. Multiplicar
df['total_venda'] = df['quantidade'] * df['preco_unitario']

# 5. Verificar tipo final
print(df['total_venda'].dtype)  # deve retornar float64

#grafico de barra simples 
df['categoria'].value_counts().plot(kind='bar')

#plt.show()

#histograma dd distribuicao de vendas
df['total_venda'].plot(kind=('hist'), bins = 20)

#plt.show()

plt.figure(figsize=(8, 6))
df['total_venda'].hist(bins=20)
plt.title('distribuicao de vendas')
plt.xlabel('valor da vendas')
plt.ylabel('frequencia')
plt.show()

#grafico de barras horizontais com o total venda
df['categoria'].value_counts().plot(kind='barh')
plt.show()

#criar uma nova coluna STATUS do cliente
df['status'] = np.where(df['total_venda'] > 10000, 'vip', 'nao vip')
print(df.head())

#trabalhando com as datas garantiundo que as datas estao no formato dateData
df['data_venda'] = pd.to_datetime(df['data_venda'])

#extrair as infromacoes de data
df['ano'] = df['data_venda'].dt.year
df['mes'] = df['data_venda'].dt.month
df['dia'] = df['data_venda'].dt.day
df['dia da semana'] = df['data_venda'].dt.dayofweek

#qual total das vendas?
print(df['total_venda'].sum())

#qual a media das vendas
print(df['total_venda'].mean)

#usando o groupby para fazer uma analise entre duas colunas
print(df.groupby('categoria')['total_venda'].sum())

print("===maximo de vendas por categoria===")
print(df.groupby('categoria')['total_venda'].max())

#grafico de vendas totais por mes
print(df.groupby('mes')['total_venda'].sum().plot(kind="bar"))
plt.show()

#meida por dia
df['categoria'].value_counts(normalize=True).plot(kind="pie")
plt.show()

print(df.groupby('dia da semana')['total_venda'].mean().plot(kind="bar"))
plt.show()

#grafico de dispersao do dia da semana com o total de vendas
df.plot(x='dia da semana',y='total_venda',kind="scatter")
plt.show()

#box plot da distribuicao por dia da semana
df.boxplot(column='total_venda', by='dia da semana')
plt.show()

#box plt do total de vendas por categoria
df.boxplot(column='total_venda', by='categoria')
plt.show()

df.boxplot(column='total_venda', by='mes')
plt.show()

#comparando o tcket medio de vendas entre vip e nao vip
print(df.groupby("status")['total_venda'].mean())

#comparando o valor total vendido por status
print(df.groupby('status')['total_venda'].sum())

#comparando as compras dos vips e nao vips por categoria
print(df.groupby(['status', 'categoria'])['total_venda'].sum())

#conclusao da estrategia 
print(df.groupby('status')['total_venda'].sum().plot(kind='pie'))
plt.show()


df.groupby("status")["total_venda"].sum().plot(kind='bar')
plt.show()