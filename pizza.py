# -*- coding: utf-8 -*-
"""PIZZA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qtNYsWtyXwUBzfbAKG1zcl1dBI7PLqta
"""

import numpy as np
import pandas as pd
import plotly.express as px

SET = ['Agricultura', 'Bunker Fuels' , 'Industrial Processes' ,'Land-Use Change and Forestry', 'Waste']

QUANT = [ 5817.65 ,  1311.60,  2902.68, 1387.56,  1606.86]

px.pie(names=SET, values=QUANT)