from dash.dcc import Graph
from dash.resources import Css
import plotly.graph_objects as go
import pandas as pd
import dash_html_components as html
import dash as dbc
    
# Lendo as bases de dados:
dados_paralel = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/ghg-emissions%201.1.csv')
dados_pizza = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1%20(2).csv')
dados_barra = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/Dados.csv')
dados_linha = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2_variacao_setores.csv')
dados_linha2 = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/annual-co2-emissions-per-country(4).csv')

# Transformando a base em uma lista de valores.
dados_paralel_array = dados_paralel.values
dados_pizza_array = dados_pizza.values
dados_barra_array = dados_barra.values
dados_linha_array = dados_linha.values
dados_linha2_array = dados_linha2.values
# print(dados_barra_array)

# ----------COORDENADAS PARALELAS----------
# Transformando a base de dados em listas separadas-
anoP = []
industria = []
calor_eletrici = []
construcao = []
transporte = []
for elemento in dados_paralel_array:
    anoP.append(elemento[0])
    industria.append(elemento[1])
    calor_eletrici.append(elemento[2])
    construcao.append(elemento[3])
    transporte.append(elemento[4])

# Plotando o gráfico:
paralel = go.Parcoords(
        line = dict(color = anoP,
        colorscale = 'turbo',
        colorbar = dict(title = 'Ano'),
        showscale = True),
        dimensions = list([
            dict(range = [min(industria), max(industria)],
            label = 'Processos Industriais (Mt)', values = industria),
            dict(range = [min(calor_eletrici), max(calor_eletrici)],
            label = 'Calor e Eletricidade (Mt)', values = calor_eletrici),
            dict(range = [min(construcao), max(construcao)],
            label = 'Construções (Mt)', values = construcao),
            dict(range = [min(transporte), max(transporte)],
            label = 'Transporte (Mt)', values = transporte)]
            )
)


# Criando a imagem do gráfico plotado:
graf_paralel = go.Figure(paralel)
# Modificando o lyout geral do gráfico (cor de fundo):
graf_paralel.update_layout(
    #title_text = 'Emissões de Setores Específicos no Brasil (1990-2018)',
    template = 'plotly_dark',
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor='rgba(0,0,0,0)'
)

# ----------PIZZA----------
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
    soma = sum(lista)
    Values.append(int(soma)/len(gas))

labels = ['Gasolina' , 'Carvão',  'Cimento' ,'Queimadas', 'Óleo']
colors = ['gold', 'Crimson', 'LightSlateGray', 'Black', 'Chartreuse']

pizza = go.Pie(
    labels = labels,
    values = Values,
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
    #title_text = 'Emissões de CO2 em Setores de Combustíveis <br><sup>Valores Referentes a Africa, Ásia, Europa, Oceania, América do Norte e América do Sul (1990-2018)</sup>',
    title_font_size = 30,
    template = 'plotly_dark',
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor='rgba(0,0,0,0)',
)

# ----------BARRA----------
year = []
mundo = []
brasil = []
for linha in dados_barra_array:
    year.append(linha[0])
    mundo.append(linha[1])
    brasil.append(linha[2])

graf_barra = go.Figure()
graf_barra.add_trace(go.Bar(x = year, y = mundo, name = 'Mundo'))
graf_barra.add_trace(go.Bar(x = year, y = brasil, name = 'Brasil'))

# Personalização do gráfico de barras
graf_barra.update_layout(
    #title = 'Concentração de CO2 na Atmosfera: Brasil/Mundo (1991-2018)',
    xaxis_tickfont_size = 14,
    yaxis = dict(
        title = '(Toneladas Métricas Per Capita)',
        titlefont_size = 16,
        tickfont_size = 14,
    ),
    barmode = 'group',
    bargap = 0.15, 
    bargroupgap = 0.1,
    template = 'plotly_dark',
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor='rgba(0,0,0,0)'
)


# ----------LINHA----------
Ano = []
Energia = []
Pi = []
Agricultura = []
Solo = []
for i in dados_linha_array:
    Ano.append(i[0])
    Energia.append(i[1])
    Pi.append(i[2])
    Agricultura.append(i[3])
    Solo.append(i[4])

trace1 = go.Scatter(x = Ano, y = Energia, mode = 'lines+markers', name = 'Energia')
trace2 = go.Scatter(x = Ano, y = Pi, mode = 'lines+markers', name = 'Processos Industriais')
trace3 = go.Scatter(x = Ano, y = Agricultura, mode = 'lines+markers', name = 'Agricultura')
trace4 = go.Scatter(x = Ano, y = Solo, mode = 'lines+markers', name = 'Solo e Silvicultura')

data = [trace1,trace2,trace3,trace4]

layout = go.Layout(
    hovermode = "x",
    #title = 'Variação da Emissão de CO2 em Setores (Brasil, 1990-2018)', 
    xaxis_title = 'Anos', 
    yaxis_title = 'Variação (%)',
    font = {'family': 'Arial','size': 16}
    )
graflinha = go.Figure(data = data, layout = layout)

graflinha.update_layout(
    template = 'plotly_dark',
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor='rgba(0,0,0,0)'
)


# ----------LINHA----------
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
    #title_text = 'Concentração de CO2: Alemanha, America do sul, Asia, Brasil, China, Europa, EUA (1990-2018)',
    template = 'plotly_dark',
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis = dict(title = "Anos"),
    yaxis = dict(title = 'Concentração de CO2')
)  


'''graf_paralel.show()
graf_pizza.show()
graflinha2.show()
graf_barra.show()
graflinha.show()'''

# Aqui começa a implementação dos gráficos em dash:

# Separando os dados já filtrados do gráfico de Pizza para que cada país tenha suas próprias listas de cada setor:

proc = [oleo, queimada, cement, carvao, gas]

oleoAf = []
oleoAs = []
oleoEuro = []
oleoNA = []
oleoOc = []
oleoSA = []
espoleo = [oleoAf, oleoAs, oleoEuro, oleoNA, oleoOc, oleoSA]
for lista in espoleo:
    for num in oleo[0:29]:
        lista.append(num)
    del oleo[0:29]

queimadaAf = []
queimadaAs = []
queimadaEuro = []
queimadaNA = []
queimadaOc = []
queimadaSA = []
espqueimada = [queimadaAf, queimadaAs, queimadaEuro, queimadaNA, queimadaOc, queimadaSA]
for lista in espqueimada:
    for num in queimada[0:29]:
        lista.append(num)
    del queimada[0:29]

cementAf = []
cementAs = []
cementEuro = []
cementNA = []
cementOc = []
cementSA = []
espcement = [cementAf, cementAs, cementEuro, cementNA, cementOc, cementSA]
for lista in espcement:
    for num in cement[0:29]:
        lista.append(num)
    del cement[0:29]

carvaoAf = []
carvaoAs = []
carvaoEuro = []
carvaoNA = []
carvaoOc = []
carvaoSA = []
espcarvao = [carvaoAf, carvaoAs, carvaoEuro, carvaoNA, carvaoOc, carvaoSA]
for lista in espcarvao:
    for num in carvao[0:29]:
        lista.append(num)
    del carvao[0:29]

gasAf = []
gasAs = []
gasEuro = []
gasNA = []
gasOc = []
gasSA = []
espgas = [gasAf, gasAs, gasEuro, gasNA, gasOc, gasSA]
for lista in espgas:
    for num in gas[0:29]:
        lista.append(num)
    del gas[0:29]

# Utilizando o dash de fato:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

css = ['https://bootswatch.com/4/darkly/bootstrap.css']



markdown_H1 = '''
            O intuito desta página é analisar as emissões e concentrações de CO2 (gás carbônico) na atmosfera por meio de gráficos demonstrativos e comparativos. Os gráficos focam no período de tempo de 1990 a 2018 especialmente no Brasil, apesar de trazer dados referentes a outras regiões do mundo. Bases de dados e códigos disponíveis publicamente [neste repositório do GitHub](https://github.com/EdPPF/APC-Parte01).
            '''

markdown_paralel = '''
            O gráfico de Coordenadas paralelas pemrite comparar variáveis de dimensões diferentes ao mesmo tempo, por meio das colunas presentes na figura. Este gráfico mostra como foram as emissões de CO2 no Brasil nos setores presentes na imagem. - Base de dados disponível em [ghg-emissions 1.1.csv](https://github.com/EdPPF/APC-Parte01/blob/main/ghg-emissions%201.1.csv).
            '''

markdown_pizza = '''
            A proposta do próximo gráfico é comparar dados de emissões de CO2 referentes a várias regiões do mundo, de modo a calcular a média dessas regiões para cada setor específico. - Base de dados disponível em [co2-emissions-by-fuel-line_1 (2).csv](https://github.com/EdPPF/APC-Parte01/blob/main/co2-emissions-by-fuel-line_1%20(2).csv).
            '''
submarkdown_pizza = '''
            A base de dados para este gráfico é extensa, contendo dados referentes aos anos de 1750 até 2019, além de a vários países e regiões do mundo. Dessa forma, os dados foram filtrados para apresentar apenas valores Referentes a  Africa, Ásia, Europa, Oceania, América do Norte e América do Sul. Com esses dados, foi feita a média das emissões para cada setor presente no gráfico, de maneira a permitir uma rápida comparação de valores. Abaixo podem ser conferidos os dados referentes a cada país: ...ou será que podem?
            '''

markdown_linha2 = '''
            De maneira similar ao anterior, o gráfico abaixo apresenta as emissões anuais de CO2 para as mesmas regiões, permitindo uma análise mais geral e precisa entre elas, não restrita a setores específicos. Também foi adicionada uma linha, "Mundo", referente a emissões globais de CO2. - Base de dados disponível em [annual-co2-emissions-per-country(4).csv](https://github.com/EdPPF/APC-Parte01/blob/main/annual-co2-emissions-per-country(4).csv).
            '''

markdown_barra = '''
            Este gráfico compara as concentrações per capita de CO2 na atmosfera no Brasil e o total mundial. - Base de dados disponível em [Dados.csv](https://github.com/EdPPF/APC-Parte01/blob/main/Dados.csv).
            '''

markdown_linha = '''
            Por fim, o gráfico a seguir demonstra como foi a variação percentual da emissão de CO2 nos setores apresentados, no Brasil. - Base de dados disponível em [co2_variacao_setores.csv](https://github.com/EdPPF/APC-Parte01/blob/main/co2_variacao_setores.csv).
            '''

markdown_creditos = '''
            ***  
            Aline Melo (), Eduardo Pereira (19/0026987), Fause Carlos (), Felipe Figueiredo (), Isaac Lucas (), 
            Laiza Daniele (), Leandro de Souza (), Maykon Junio ()  
            Algoritmos e Programação de Computadores - 01/2021  
            Grupo 12
            '''

# Titulo
external_stylesheets = [
    'https://bootswatch.com/4/darkly/bootstrap.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.Div(children=[
        html.Div([
            html.H1(
                children='Avaliação das Emissões e Concentrações de CO2',
                style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
                }
            ),
            dcc.Markdown(
                children=markdown_H1,
                style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
        ]),
    ],
    style={  
        'color': '#fff',
        'background-color': '#3c4043',
        'padding': '10px 10px',
        'border-radius': '10px',
        'margin-top': '7px',
        'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
    } #Estilo DIV titulo
    ), 

# Grafico 1

    html.Div(children=[
        html.Div([
            html.H1(
                children='Emissões de Setores Específicos no Brasil (1990-2018)',
                style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
                    
                }
            ),
            dcc.Markdown(
                children=markdown_paralel,
                style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
            dcc.Graph(
                figure=graf_paralel,
                style={
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                },
                config={
                    'displayModeBar': False,
                    'displaylogo': False,
                }
            )
        ]),
    ],
    style={
        'color': '#fff',
        'background-color': '#3c4043',
        'padding': '10px 10px',
        'border-radius': '10px',
        'margin-top': '7px',
        'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
    } #Estilo paralelo DIV
    ),

        # Grafico 2

        html.Div(children=[
            html.Div([  # Bloco para o título e o primeiro markdown.
                html.H1(
                    children='Emissões de CO2 em Setores de Combustíveis (1990-2018)',
                    style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
                    }
                ),
                dcc.Markdown(
                    # children=markdown_pizza,
                    style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                    }
                ),
            ]),

            html.Div([  # Bloco para o gráfico. Está separado pois é necessário adicionar 'display' em style.
                dcc.Graph(
                    figure=graf_pizza,
                    style={
                        'font-size':'20px',
                        'width' : '90%',
                        'margin': 'auto',
                    },
                    config={
                    'displayModeBar': False
                }
                ),
            ],
                style={}
            ),

            html.Div([  # Bloco para o segundo markdown. Está separado pois é necessário adicionar 'display' em style.
                dcc.Markdown(
                    children=submarkdown_pizza,
                    style={
                        'text-indent': '70px',
                        'text-align': 'justify',
                        'font-size':'20px',
                        'width' : '90%',
                        'margin': 'auto',
                    }
                )
            ],
                style={
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
            ], style={
                'color': '#fff',
                'background-color': '#3c4043',
                'padding': '10px 10px',
                'border-radius': '10px',
                'margin-top': '7px',
                'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',

            }),
            

            html.Div(children=[
            html.Div([  # Bloco para o dropdown, Gráfico extra e texto desse gráfico.
                html.H1(
                    children='titulo',
                    style={
                        'color':'#fff', 
                        'font-size':'25px',
                        'box-shadow': '0px 0px 5px #363636',
                        'padding': '10px 20px',
                        'width':'max-content',
                        'background-color' : '#616161',
                        'border-radius': '10px',
                        'margin': '30px',
                        'margin-left': '5%',
                    }
                ),
                dcc.Dropdown(
                    id='Processo',
                    #options=[{'label': ['Óleo', 'Queimada', 'Cimento', 'Carvao', 'Gas'], 'value': [1, 2, 3, 4, 5]}],
                    options=[{'label': nome, 'value': num} for num, nome in zip([1,2,3,4,5], ['Óleo', 'Queimada', 'Cimento', 'Carvao', 'Gas'])],
                    value=1,
                    style={
                        'color':'#00bc8c',
                        'width' : '90%',
                        'margin': 'auto',
                        'background-color': '#616161',
                        'border': 'none',
                        'border-radius': '10px',
                    }
                ),
                dcc.Graph(id='linhaplus',
                style={
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                },
                config={
                    'displayModeBar': False
                }
                )
            ])
            ], 
            style={
                'color': '#fff',
                'background-color': '#3c4043',
                'padding': '10px 10px',
                'border-radius': '10px',
                'margin-top': '7px',
                'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
            }
        ),


        html.Div(children=[
            html.H1(
                children='Concentração de CO2 (1990-2018, Regiões Específicas e Mundo)',
                style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
            }
            ),
            dcc.Markdown(
                children=markdown_linha2,
                style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
            dcc.Graph(figure=graflinha2,
                style={
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                },
                config={
                    'displayModeBar': False
                }
            )
        ],
        style={
            'color': '#fff',
            'background-color': '#3c4043',
            'padding': '10px 10px',
            'border-radius': '10px',
            'margin-top': '7px',
            'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
        }
        ),

        html.Div(children=[
            html.H1(
                children='Concentração de CO2 Per Capita (1991-2018, Brasil e Mundo)',
                style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
                }
            ),
            dcc.Markdown(
                children=markdown_barra,
                style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
            dcc.Graph(
                figure=graf_barra,
                style={
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                },
                config={
                    'displayModeBar': False
                }
            )
        ],
        style={
                'color': '#fff',
                'background-color': '#3c4043',
                'padding': '10px 10px',
                'border-radius': '10px',
                'margin-top': '7px',
                'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
        }
        ),

        html.Div(children=[
            html.H1(
                children='Variação da Emissão de CO2 em Setores (1990-2018, Brasil)',
                style={
                    'color':'#fff', 
                    'font-size':'25px',
                    'box-shadow': '0px 0px 5px #363636',
                    'padding': '10px 20px',
                    'width':'max-content',
                    'background-color' : '#616161',
                    'border-radius': '10px',
                    'margin': '30px',
                    'margin-left': '5%',
                }
            ),
            dcc.Markdown(
                children=markdown_linha,
                style={
                    'text-indent': '70px',
                    'text-align': 'justify',
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                }
            ),
            dcc.Graph(
                figure=graflinha,
                style={
                    'font-size':'20px',
                    'width' : '90%',
                    'margin': 'auto',
                },
                config={
                    'displayModeBar': False
                }
            )
        ],
        style={
            'color': '#fff',
            'background-color': '#3c4043',
            'padding': '10px 10px',
            'border-radius': '10px',
            'margin-top': '7px',
            'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
        }
        ),

        html.Div(children=[
            dcc.Markdown(
                children=markdown_creditos,
                style={
                    'font-size':'12px', 
                    'color':'#ff6666', 
                    'text-align':'center',
                    'width' : '90%',
                    'margin': 'auto',
                    }
            ),
        ],
        style={
            'color': '#fff',
            'background-color': '#3c4043',
            'padding': '10px 10px',
            'border-radius': '10px',
            'margin-top': '7px',
            'box-shadow': '0px 0px 3px rgba(58, 58, 58, 0.192)',
    }
        ),
    ],
style={
    'width': '80%',
    'height': '100%',
    'margin': '0px', 
    'margin': 'auto',
}, #Estilo DIV main
)

# Aqui vem o callback:
@app.callback(
    dash.Output('linhaplus', 'figure'),
    dash.Input('Processo', 'value')
)
# Definindo o processo de criação e alteração do gfráfico de acordo com as escolhas do drop-down:
def update_graf_linhaplus(num):
    # Essas listas serão repassadas como argumento para cada linha (setor) do gráfico.
    argAf = []
    argAs = []
    argEuro = []
    argNA = []
    argOc = []
    argSA = []
    # As listas são preenchidas de acordo com a escolha do drop-down:
    if num == 1:
        argAf = oleoAf
        argAs = oleoAs
        argEuro = oleoEuro
        argNA = oleoNA
        argOc = oleoOc
        argSA = oleoSA
    elif num == 2:
        argAf = queimadaAf
        argAs = queimadaAs
        argEuro = queimadaEuro
        argNA = queimadaNA
        argOc = queimadaOc
        argSA = queimadaSA
    elif num == 3:
        argAf = cementAf
        argAs = cementAs
        argEuro = cementEuro
        argNA = cementNA
        argOc = cementOc
        argSA = cementSA
    elif num == 4:
        argAf = carvaoAf
        argAs = carvaoAs
        argEuro = carvaoEuro
        argNA = carvaoNA
        argOc = carvaoOc
        argSA = carvaoSA
    elif num == 5:
        argAf = gasAf
        argAs = gasAs
        argEuro = gasEuro
        argNA = gasNA
        argOc = gasOc
        argSA = gasSA

    linha1 = go.Scatter(x = anos, y = argAf, mode = 'lines', name = 'Africa')
    linha2 = go.Scatter(x = anos, y = argAs, mode = 'lines', name = 'Asia')
    linha3 = go.Scatter(x = anos, y = argEuro, mode = 'lines', name = 'Europa')
    linha4 = go.Scatter(x = anos, y = argNA, mode = 'lines', name = 'América do Norte')
    linha5 = go.Scatter(x = anos, y = argOc, mode = 'lines', name = 'Oceania')
    linha6 = go.Scatter(x = anos, y = argSA, mode = 'lines', name = 'América do Sul')

    imagem = [linha1, linha2, linha3, linha4, linha5, linha6]
    graf = go.Figure(imagem)
    graf.update_layout(
        template = 'plotly_dark',
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return graf

if __name__ == '__main__':
    app.run_server(debug=True)
