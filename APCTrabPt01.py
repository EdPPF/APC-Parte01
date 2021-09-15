# Gráficos para "Taxa de emissão de cada setor (pizza)(coordenadas)".

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("TrabalhoParte01\co2-emissions-by-fuel-line_1.csv")

dados_array = df.values

# print(max(df['CO2 emissions from cement']))

paises = []
oleo = []
queimada = []
cement = []
for linha in dados_array:
    paises.append(linha[0])
    oleo.append(linha[3])
    queimada.append(linha[4])
    cement.append(linha[5])

# print(paises.count(paises[0]))  # cada país aparece 270 vezes

cores = []
for elemento in range(len(paises)//270):
    for i in range(270):
        cores.append(elemento)


fig = go.Parcoords(
        line=dict(color = cores, showscale = True),
        # colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        dimensions = list([
            dict(range = [0, 12355129200],  # de onde até onde vão os valores da variável;
            constraintrange = [0, 12355129200],  # Tamanho do filtro quando o gráfico carregar;
            label = 'Por óleo', values = oleo),
            dict(range = [0, 429495561],
            constraintrange = [0, 429495561],
            label = 'Por queimadas', values = queimada),
            dict(range = [0, 1563760568],
            constraintrange = [0, 1563760568],
            label = 'Por cement??', values = cement),
        ]))

graf = go.Figure(fig)
graf.show()
