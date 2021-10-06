import plotly.graph_objects as go
import pandas as pd
    
# Lendo as bases de dados:
dados_paralel = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/ghg-emissions%201.1.csv')
dados_pizza = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1.csv')
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
ano = []
industria = []
calor_eletrici = []
construcao = []
transporte = []
for elemento in dados_paralel_array:
    ano.append(elemento[0])
    industria.append(elemento[1])
    calor_eletrici.append(elemento[2])
    construcao.append(elemento[3])
    transporte.append(elemento[4])

# Plotando o gráfico:
paralel = go.Parcoords(
        line = dict(color = ano,
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
    title_text = 'Emissões de Setores Específicos no Brasil (1990-2018)',
    template = 'plotly_dark')


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
    Values.append(int((soma)/(len(lista))))
   
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
    template = 'plotly_dark'
    )

# ----------LINHA/BARRA----------
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
    title = 'Concentração de CO2 na Atmosfera: Brasil/Mundo (1991-2018)',
    xaxis_tickfont_size = 14,
    yaxis = dict(
        title = '(Toneladas Métricas Per Capita)',
        titlefont_size = 16,
        tickfont_size = 14,
    ),
    barmode = 'group',
    bargap = 0.15, 
    bargroupgap = 0.1,
    template = 'plotly_dark'
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

layout=go.Layout(
    hovermode = "x",
    title = 'Variação da Emissão de CO2 em Setores (Brasil, 1990-2018)', 
    xaxis_title = 'Anos', 
    yaxis_title = 'Variação (%)',
    font = {'family': 'Arial','size': 16}
    )
graflinha = go.Figure(data = data, layout = layout)

graflinha.update_layout(
    template = 'plotly_dark'
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
    title_text = 'Concentração de CO2: Alemanha, America do sul, Asia, Brasil, China, Europa, EUA (1990-2018)',
    template = 'plotly_dark',
    xaxis = dict(title = "Anos"),
    yaxis = dict(title = 'Concentração de CO2')
)  


graf_paralel.show()
graf_pizza.show()
graflinha2.show()
graf_barra.show()
graflinha.show()
