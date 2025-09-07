import pandas as pd

packages = pd.read_csv('python-local-package-size.csv')
print(packages.iloc[0])

print('#--------')

print(packages.iloc[0:5])

print('#--------')

print(packages['Characters'][0:3])

print('#--------')

print(packages.iloc[0:3]['Characters'])
