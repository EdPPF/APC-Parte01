import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('annual-co2-emissions-per-country(2).csv', sep=',', usecols=['Entity','Code', 'Year', 'Annual CO2 emissions'])

#Transformando a lista em array
df_array = df.values

#criando listas vazias
pais = []
code = []
ano = []
CO2_emitido = []

#Extrutura de repetição:
for i in df_array:
  pais.append(i[0])
  code.append(i[1])
  ano.append(i[2])
  CO2_emitido.append(i[3])

#Criação e edição do gráfico
imagem = go.Figure(go.Scatter(x=ano,
                              y=CO2_emitido,
                              mode='lines',
                              text=pais))

#Acrescentando algumas características ao gráfico
graf_linha = go.Figure(imagem)
graf_linha.update_layout(
    title_text='Emissão de CO2: Alemanha, America do sul, Asia, Brasil, China, Europa, EUA',
    template = 'plotly_dark',
    xaxis = dict(
        title = "Anos"),
    yaxis = dict(
        title = 'Concentração de CO2'
    )
)
    

graf_linha.show()
