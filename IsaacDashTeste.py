from dash.html.Figcaption import Figcaption
from dash.html.Figure import Figure
import plotly.graph_objects as go
import pandas as pd
    
# Lendo as bases de dados:
dados_linha2 = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/annual-co2-emissions-per-country(4).csv')

# Transformando a base em uma lista de valores.
dados_linha2_array = dados_linha2.values

ano = []
asia = []
brasil = []
china = []
europa = []
alemanha = []
americsul = []
usa = []
world = []
for i in dados_linha2_array:
    ano.append(i[0])
    asia.append(i[1])
    brasil.append(i[2])
    china.append(i[3])
    europa.append(i[4])
    alemanha.append(i[5])
    americsul.append(i[6])
    usa.append(i[7])
    world.append(i[8])

linha1 = go.Scatter(x = ano, y = asia, mode = 'lines', name = 'Asia')
linha2 = go.Scatter(x = ano, y = brasil, mode = 'lines', name = 'Brasil')
linha3 = go.Scatter(x = ano, y = china, mode = 'lines', name = 'China')
linha4 = go.Scatter(x = ano, y = europa, mode = 'lines', name = 'Europa')
linha5 = go.Scatter(x = ano, y = alemanha, mode = 'lines', name = 'Alemanha')
linha6 = go.Scatter(x = ano, y = americsul, mode = 'lines', name = 'America do Sul')
linha7 = go.Scatter(x = ano, y = usa, mode = 'lines', name = 'Estados Unidos')
linha8 = go.Scatter(x = ano, y = world, mode = 'lines', name = 'Mundo')

imagem = [linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8]

graflinha2 = go.Figure(imagem)

graflinha2.update_layout(
    template = 'plotly_dark',
    xaxis = dict(title = "Anos"),
    yaxis = dict(title = 'Concentração de CO2')
)  

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Concentração de CO2'),

    html.Div(children='''
    Alemanha, America do sul, Asia, Brasil, China, Europa, EUA (1990-2018)'''),

    dcc.Graph(
        id='OhNo',
        figure = graflinha2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
