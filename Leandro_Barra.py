'''
Gráfico de barras,
Concentração de CO2 na atmosfera(Metric Tons Per Capita), base de dados retirado do site: 
https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?locations=BR-1W
'''
#importação das bibliotecas
import plotly.graph_objects as go
import pandas as pd # Utilização do pandas para usar a base de dados no formato CSV

#Base de dados utilizado para a construção dos gráficos
dados = pd.read_csv('https://raw.githubusercontent.com/Leanddro13/Leandro-Silva/main/Dados.csv')
dados_data = dados.values

year = []
mundo = []
brasil = []

# Estruturas de repetição
for linha in dados_data:
    year.append(linha[0])
    mundo.append(linha[1])
    brasil.append(linha[2])

# Criação do gráfico de barras
fig = go.Figure()
fig.add_trace(go.Bar(x= year, y= mundo, name='mundo'))
fig.add_trace(go.Bar(x= year, y= brasil, name='Brasil'))

# Personalização do gráfico de barras
fig.update_layout(
    title='Concentração de CO2 na atmosfera',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='(Metric Tons Per Capita)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, 
    bargroupgap=0.1 
)
# fig.show() não funcionou no meu Vscode

# Utilização do dash para rodar o gráfico na Web

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False) 
