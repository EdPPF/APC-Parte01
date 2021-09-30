import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('annual-co2-emissions-per-country.csv', sep=',', usecols=['Code', 'Year', 'Annual CO2 emissions'])

df_array = df.values

#criando listas vazias
pais = []
ano = []
CO2_emitido = []

#Extrutura de repetição:
for i in df_array:
  pais.append(i[0])
  ano.append(i[1])
  CO2_emitido.append(i[2])
  
criacao_grafico = go.Scatter(
    x = ano,
    y = CO2_emitido
)

grafico = go.Figure(criacao_grafico)
grafico.show()
