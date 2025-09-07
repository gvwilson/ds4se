import pandas as pd
import plotly.express as px

packages = pd.read_csv('python-local-package-size.csv')
packages = packages[packages['Lines'] > 0]
packages['ratio'] = packages['Characters'] / packages['Lines']

fig = px.histogram(packages, x='ratio')
fig.show()
fig.write_image('figures/hist-ratio-unscaled.svg', width=600, height=400)

#--------

fig = px.histogram(packages, x='ratio', nbins=100, log_y=True)
fig.show()
fig.write_image('figures/hist-ratio-scaled.svg', width=600, height=400)

#--------

print(f"Excluding {len(packages[packages['ratio'] > 100])}/{len(packages)} data points")
fig = px.histogram(packages[packages['ratio'] <= 100], x='ratio', nbins=100)
fig.show()
fig.write_image('figures/hist-ratio-most.svg', width=600, height=400)
