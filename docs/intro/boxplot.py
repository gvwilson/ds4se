#!/usr/bin/env python

import pandas as pd
import plotly.express as px

df = pd.read_csv('jccpprtTR.csv')
fig = px.box(df, y='whours', points='all')
fig.write_image('boxplot.svg', width=600, height=400)
