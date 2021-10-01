import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('/content/annual-co2-emissions-per-country(3) - annual-co2-emissions-per-country(3).csv', sep=',')

#Transformando a lista em array
df_array = df.values

#criando listas vazias para manipular depois
ano = []
asia = []
brasil = []
china = []
europa = []
alemanha = []
americsul = []
usa = []
world = []


#Extrutura de repetição:
for i in df_array:
  ano.append(i[0])
  asia.append(i[1])
  brasil.append(i[2])
  china.append(i[3])
  europa.append(i[4])
  alemanha.append(i[5])
  americsul.append(i[6])
  usa.append(i[7])
  world.append(i[8])
#Criação e edição do gráfico / Eixo x
#Definindo qual valor será representado no eixo Y.
#mode define o tipo de linha que o gráfico terá. 
#name define o padrão que as linhas armazenará, e nesse caso será o nome de cada país.
linha1 = go.Scatter(x=ano, y= asia, mode = 'lines', name = 'Asia')
linha2 = go.Scatter(x = ano, y = brasil, mode = 'lines', name = 'Brasil')
linha3 = go.Scatter(x = ano, y = china, mode = 'lines', name = 'China')
linha4 = go.Scatter(x = ano, y = europa, mode = 'lines', name = 'Europe')
linha5 = go.Scatter(x=ano, y= alemanha, mode = 'lines', name = 'Germany')
linha6 = go.Scatter(x = ano, y = americsul, mode = 'lines', name = 'South America')
linha7 = go.Scatter(x = ano, y = usa, mode = 'lines', name = 'United States')
linha8 = go.Scatter(x = ano, y = world, mode = 'lines', name = 'World')

#Definindo as listas como imagem para facilitar na manipulação
imagem = [linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8]

#Comando que permite a manipulação das características do gráfico 
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
#Title representa o "Nome principal" Do gráfico
#Template altera o tema de fundo do gráfico
#Xaxis e Yaxis acrescentam, respectivamente, o nome do eixo x e o y do gráfico

#Executa o gráfico
graf_linha.show()
