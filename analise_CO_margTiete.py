#Dados de CO - CETESB - 2019 a 2022

#Importando as bibliotecas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Para a leitura dos dados, temos:
#Arquivo xlsx disponível no repositório

dt = pd.read_excel(r'')

#Trabalhando os dados, podemos ver o dataframe tem muitas colunas, então vamos filtrar para selecionarmos apenas as que vamos estudar

dt.drop(['Tipo de Rede', 'Tipo de Monitoramento', 'Tipo', 'Nome Parâmetro', 'Código Estação', 'Nome Estação', 'Média Móvel', 'Válido', 'Dt. Amostragem', 'Dt. Instalação', 'Dt. Instalação', 'Dt. Retirada', 'Concentração', 'Taxa'], axis = 1, inplace = True)
dt = dt[dt['Unidade Medida'] == 'ppm']

#Como vamos fazer uma análise temporal, vamos juntar as colunas de Data e Hora, e trasformar em um index ('DATE_TIME') concatenando as colunas

dt = dt.set_index('Data')
dt.index = pd.to_datetime(dt.index)
dt['DATE'] = dt.index.strftime('%Y-%m-%d')
dt['DATE_TIME'] = dt['DATE'].map(str) + ' ' + dt['Hora'].map(str)

#Vamos tirar as colunas Data e Hora para não ficar repetitivo, e setar o novo index ('DATE_TIME')

dt = dt.set_index('DATE_TIME')
dt = dt.drop_duplicates()
dt = dt.sort_index()
dt.index = pd.to_datetime(dt.index, utc = True)


#Com a manipulação e filtragem dos dados, vamos plotar os gráficos para análise

dt['hour'] = dt.index.strftime('%H')
dt['hour'] = pd.Categorical(dt['hour'], categories = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], ordered = True)
dt['Year'] = dt.index.strftime('%Y')
dt.columns = ['unidade_medida', 'media_horaria', 'hour', 'year']

#Agora mudando o parâmetro x conseguimos diferentes tipos de gráfico

fig, ax = plt.subplots(figsize = (9,7))
bx = sns.lineplot(data = dt, x = 'hour', y = 'media_horaria', hue = 'year', ci = 95)

#Títulos
plt.title('... Station - Average ... cycle', fontsize = 16)
plt.xlabel('hour', fontsize = 16)
plt.ylabel('$CO_{} \; (ppm)$', fontsize = 16)

# tamanho dos valores dos eixos
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# grid do gráfico
plt.grid(axis='both', which='major', linestyle='-')
