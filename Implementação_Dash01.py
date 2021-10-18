from dash.dcc import Graph
from dash.resources import Css
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

dados_pizza = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1%20(2).csv')
dados_pizza_array = dados_pizza.values

paises = []
anos = []
oleo = []
queimada = []
cement = []
carvao = []
gas = []
for elemento in dados_pizza_array:
    paises.append(elemento[0])
    anos.append(elemento[2])
    oleo.append(elemento[3])
    queimada.append(elemento[4])
    cement.append(elemento[5])
    carvao.append(elemento[6])
    gas.append(elemento[7])

# Filtrando os dados para o gráfico de pizza:
listas = [paises, anos, oleo, queimada, cement, carvao, gas]
for lista in listas:
    del lista[:510]  # - Africa, 1990
    del lista[29:2700]  # Africa, 2018 - Asia, 1990
    del lista[58:15419]  # Asia, 2018 - Europe, 1990
    del lista[87:22468]  # Europe, 2018 - North America, 1990
    del lista[116:1437]  # North America, 2018 - Oceania, 1990
    del lista[145:10106]  # Oceania, 2018 - South America, 1990
    del lista[174:]  # South America, 2018 -

# Criando outra lista de listas para trabalhar com elas individualmente:
listas_sub = [gas, carvao, cement, queimada, oleo]

# "Values" armazenará os valores das médias que compõem o gráfico
Values = []
# Calculando os somatórios dos valores em cada lista e armazenando as médias em Values: 
for lista in listas_sub:
    soma = 0
    '''for nota in lista:
        soma += nota'''
    soma = sum(lista)
    Values.append(int(soma)/len(gas))

labels = ['Gasolina' , 'Carvão',  'Cimento' ,'Queimadas', 'Óleo']
colors = ['gold', 'Crimson', 'LightSlateGray', 'Black', 'Chartreuse']

pizza = go.Pie(
    labels = labels,
    values = Values
    )

graf_pizza = go.Figure(pizza)
graf_pizza.update_traces(
    textfont_size = 15,
    marker = dict(
        colors = colors,
        line = dict(color = '#4169E1', width = 2)
        )
    )

graf_pizza.update_layout(
    title_text = 'Emissões de CO2 em Setores de Combustíveis <br><sup>Valores Referentes a Africa, Ásia, Europa, Oceania, América do Norte e América do Sul (1990-2018)</sup>',
    title_font_size = 30,
    template = 'plotly_dark'
    )


# Aqui começa a implementação em dash.
css = ['https://bootswatch.com/4/darkly/bootstrap.css']

app = dash.Dash(__name__, external_stylesheets=css)
app.layout = html.Div([
    html.Div([
        html.H1(
            children='Avaliação das Emissões e Concentrações de CO2',
            style={'color':'#2acaea','font-size':'30px', 'text-align':'center'}
            ),
        html.Div(
            children='O objetivo desse trabalho é bla bla bla bla '+
            'Título, centralizado (feito com "html.H1") '+
            'texto introdutório e explicativo (feito com "html.Div"?) '+
            'Várias seções, cada uma contendo um gráfico: '+
            'Todos os gráficos sguirão o mesmo padrão: um texto que o explica '+
            'seguido da figura do gráfico. O único que será diferente é '+
            'o de pizza. Ele ficará ao lado do texto que o explica. Logo em '+
            'seguida virá o gráfico de linha, que é o do Issac. Esse gráfico '+
            'será atualizado em tempo real, se conseguirmos descobrir como '+
            'fazer isso (só pra ficar legal).',
            style={'font-size':'15px', 'text-align':'center'}
            ),
    ]),

    html.Br(),

    html.Div([
        html.Br(),
        dcc.Graph(
            id='pizza',
            figure = graf_pizza,
            ),
        html.Br(),
        html.Div(
            'O gráfico acima é legal e tudo mais. Ele demonstra bla bla bla',
            style={'font-size':'15px'}
        )
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
