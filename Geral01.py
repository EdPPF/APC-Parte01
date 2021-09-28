import plotly.graph_objects as go
import pandas as pd

# GRÁFICO COORDENADAS PARALELAS:
    
# Lendo as bases de dados:
dados_paralel = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/ghg-emissions%201.1.csv')
dados_pizza = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1.csv')

# Transformando a base em uma lista de valores.
    # "values() is an inbuilt method in Python that returns a list of all the values available in a given dictionary"
dados_paralel_array = dados_paralel.values
dados_pizza_array = dados_pizza.values


# ----------COORDENADAS PARALELAS----------
# Cada linha do gráfico é um ano, de 1990 até 2018, do Brasil. Cada coluna refere-se a valores da emissão de
    # CO2 do Brasil nesse setor e ano específicos. 
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

# A lista "ano" será usada para determinar as cores de cada linha no gráfico. Isso é válido pois essa lista contém
    # apenas valores numéricos.
# Plotando o gráfico:
    # Unidade das variáveis: Mt = Megaton = Um milhão de toneladas
paralel = go.Parcoords(
        line=dict(color = ano,  # 'color' vai receber uma lista e distribuir à cada linha que aparecer no gráfico uma cor;
        colorscale='turbo',  # 'colorscale' define a escala das cores (as cores de fato);
        colorbar=dict(title='Ano'),  # 'colorbar' recebe um dict() para definir algumas propriedades da escala (no caso, o título);
        showscale = True),  # 'showscale' mostra a escala de cores conforme os valores numéricos (barra direita na figura);
        dimensions = list([
            dict(range = [min(industria), max(industria)],  # 'range' define de onde até onde vão os valores dessa variável específica;
            label = 'Processos Industriais (Mt)', values = industria),  # Nome do eixo dessa variável e quais dados da bse de dados aparecerão aqui;
            dict(range = [min(calor_eletrici), max(calor_eletrici)],
            label = 'Calor e Eletricidade (Mt)', values = calor_eletrici),
            dict(range = [min(construcao), max(construcao)],
            label = 'Construções (Mt)', values = construcao),
            dict(range = [min(transporte), max(transporte)],
            label = 'Transporte (Mt)', values = transporte)])
)

# Criando a imagem do gráfico plotado:
graf_paralel = go.Figure(paralel)
# Modificando o lyout geral do gráfico (cor de fundo):
graf_paralel.update_layout(
    title_text='Emissões de Setores Específicos no Brasil (1990-2018)',
    template = 'plotly_dark')

# ----------PIZZA----------
# Transformando a base de dados em listas separadas-
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
    del lista[:3210]
    del lista[29:5130]
    del lista[58:3539]
    del lista[87:6808]
    del lista[116:3597]
    del lista[145:19016]
    del lista[174:11485]
    del lista[203:8004]
    del lista[232:]

# Criando outra lista de listas para trabalhar com elas individualmente:
listas_sub = [gas, carvao, cement, queimada, oleo]

# "Values" armazenará os valores das médias que compõem o gráfico
Values = []
# Calculando os somatórios dos valores em cada lista e armazenando as médias em Values: 
for lista in listas_sub:
    soma = 0
    for nota in lista:
        soma += nota
    Values.append(int(soma)/232)

labels = ['Gasolina' , 'Carvão',  'Cimento' ,'Queimadas', 'Óleo']
colors = ['gold', 'Crimson', 'LightSlateGray', 'Black', 'Chartreuse']

pizza = go.Pie(
    labels=labels,
    values=Values
    )

graf_pizza = go.Figure(pizza)
graf_pizza.update_traces(
    textfont_size=15,
    marker=dict(colors=colors, line=dict( color='#4169E1',width=2 ))
    )

graf_pizza.update_layout(
    title_text='Emissões de CO2 em Setores de Combustíveis <br><sup>Valores referentes a Ásia, América, Europa e Brasil, China, EUA e Alemanha (1990-2018)</sup>',
    template = 'plotly_dark')

graf_pizza.show()
graf_paralel.show()
