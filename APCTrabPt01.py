# Gráficos para "Taxa de emissão de cada setor (pizza)(coordenadas)".

import plotly.graph_objects as go
import pandas as pd

# Lendo a base de dados:
df = pd.read_csv("TrabalhoParte01\co2-emissions-by-fuel-line_1.csv")
# Transformando a base em um array para ser devidamente manipulado:
dados_array = df.values

# Usei isso aqui pra definir a escala dos eixos do gráfico:
# print(max(df['CO2 emissions from cement']))  

# Criando as listas que armazenarão cada coluna da base de dados (fazemos isso pois não podemos utilizar os
    # elementos da base de dados usando o pandas direto, como em df[Entity], que já retorna toda a coluna 'Entity'
    # da base de dados).
paises = []
oleo = []
queimada = []
cement = []
# Faltam as outras colunas.
for linha in dados_array:
    paises.append(linha[0])
    oleo.append(linha[3])
    queimada.append(linha[4])
    cement.append(linha[5])

# print(paises.count(paises[0]))  # cada país aparece 270 vezes

# Para o gráfico de Coordenadas Paralelas, a ideia é que cada variável, que no caso são os países, tenha uma cor
    # diferente. Aqui, estou criando uma lista vazia que armazenará valores numéricos de cores para cada elemento
    # da lista 'paises'. Isso já sabendo que cada país aparece na base de dados 270 vezes.
cores = []
for elemento in range(len(paises)//270):
    for i in range(270):
        cores.append(elemento)


# Plotando o gráfico:
fig = go.Parcoords(
        line=dict(color = cores, showscale = True),  # 'color' vai receber uma lista e distribuir à cada variável
                                                        # que aparecer no gráfico uma cor. O 'showscale' mostra
                                                        # a escala de cores conforme os valores numéricos (barra direita na figura);
        dimensions = list([
            dict(range = [0, 12355129200],  # 'range' define de onde até onde vão os valores dessa variável específica;
            constraintrange = [0, 12355129200],  # Tamanho do filtro quando o gráfico carregar;
            label = 'Por óleo', values = oleo),  # Nome do eixo dessa variável e quais dados da bse de dados aparecerão aqui;
            dict(range = [0, 429495561],
            constraintrange = [0, 429495561],
            label = 'Por queimadas', values = queimada),
            dict(range = [0, 1563760568],
            constraintrange = [0, 1563760568],
            label = 'Por cement??', values = cement),
        ]))

# Criando a imagem do gráfico plotado:
graf = go.Figure(fig)
# Mostrando a imagem:
graf.show()
