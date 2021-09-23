# -*- coding: utf-8 -*-
"""PIZZA PX

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qtNYsWtyXwUBzfbAKG1zcl1dBI7PLqta
"""

import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/EdPPF/APC-Parte01/main/co2-emissions-by-fuel-line_1.csv')

#função para tirar a Media das emissões 

F = df.groupby('Year').mean().tail()
F.drop([2015,2016,2017,2018]).values

# os valores de F = array(178790291e+08, 690167088e+06, 224574731e+07, 206240903e+08,125593648e+08, 210673718e+06)
# Ao tirar a média tive problema com a formatação, por isso criei a função 'Values' para copiar os valores formatados

SET = ['óleo' , 'Queimadas' , 'Cimento' ,'Carvão', 'Gasolina', 'Outras Industrias']

Values = [ 1787903 ,  6901671,  2245747, 2062409,  1255936 , 2106737 ]

#color_discrete_sequence=px.colors.sequential.RdBu = função para pintar o graficos das cores usadas 

fig = px.pie(names=SET, values=Values,color_discrete_sequence=px.colors.sequential.RdBu,title='EMISSÕES DE CO2 NOS SETORES DE COMBUSTÍVEIS')
fig.show()