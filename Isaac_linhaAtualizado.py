import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('annual-co2-emissions-per-country(2).csv', sep=',', usecols=['Entity','Code', 'Year', 'Annual CO2 emissions'])

#Transformando a lista em array
df_array = df.values

#criando listas vazias para manipular depois
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

#Criação e edição do gráfico / Eixo x
#Definindo qual valor será representado no eixo Y.
#mode define o tipo de linha que o gráfico terá. 
#text define o padrão que as linhas armazenará, e nesse caso será o nome dos países.
imagem = go.Figure(go.Scatter(x=ano,                         
                              y=CO2_emitido,
                              mode='lines',
                              text=pais))

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
