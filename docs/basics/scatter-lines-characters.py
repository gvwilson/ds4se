import pandas as pd
import plotly.express as px

packages = pd.read_csv('python-local-package-size.csv')
fig = px.scatter(packages, x='Lines', y='Characters')
fig.show()
fig.write_image('figures/scatter-lines-characters.svg')
