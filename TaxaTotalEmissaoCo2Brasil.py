'''
Codigo feito no Colab.
https://colab.research.google.com/drive/1b8SsfiOrWY-c4w5HhmX_wjtUO1XWXkg8?usp=sharing
'''

import plotly.express as px #biblioteca para trabalhar com os graficos
import numpy #biblioteca para fazer os calculos matematicos 

dados_x = ['2013', '2014', '2015', '2016', '2017', '2018' ]  #Os dados que serão aprensentados no grafico
dados_y = ['360.83', '385.38', '362.64', '334.14', '336.36', '317.82']
  
fig = px.pie(names = dados_x, values = dados_y, width = 500, height = 500, title = 'Taxa total de emissão de Co2 no Brasil por ano', # px.pie transforma o grafico em pizza
 color_discrete_sequence = px.colors.sequential.RdBu) #Tambem pode ser feita a personalização do grafico no px.pie
fig.show() #mostrar a figura
