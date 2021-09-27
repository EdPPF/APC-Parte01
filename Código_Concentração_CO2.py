# ------------------------------ Concentração de CO2 na Atmosfera ------------------------------ #
# ______________________________________ Gráfico de barra ______________________________________ #

# 1. Importando as bibliotecas
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# 2. Criando listas vazias
anos = []
ppm = []

# 3. Importando os dados usando o pandas
dados = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/DataFrame_Concentra%C3%A7%C3%A3o_CO2')

# 4. Transformando os dados em Array
dados_a = dados.values

# 5. Organizando os dados em listas distintas
for x in dados_a:
    anos.append(x[0])
    ppm.append(x[1])

# 6. Criando uma figura com os gráficos
co2 = go.Figure(data=[
    go.Scatter(
        x = anos, 
        y = ppm, 
        name = 'Linha',
        marker_color='#FAD41B',
        
    ),
    go.Bar(
        x = anos, 
        y = ppm, 
        name = 'Barra',
        marker_color = '#76777B',
    )   
])

# 7. Definindo o layout da figura
co2.update_layout(
    title = 'Concentração de CO2 na Atmosfera',
    template = 'plotly_dark',
    yaxis = dict(
        title = 'PMM (partes por milhão)',
    ),
    xaxis = dict(
        title = 'Anos',
    )
)

# 8. Exibindo a figura
co2.show()

# ______________________________________________________________________________________________ #
