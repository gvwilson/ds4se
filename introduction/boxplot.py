#!/usr/bin/env python

import pandas as pd
import plotly.express as px

df = pd.read_csv('data/jccpprtTR.csv')
fig = px.box(df, y='whours', points='all')
fig.write_image('figures/boxplot.svg', width=600, height=400)
