import pandas as pd

colors = pd.DataFrame(columns=['name', 'red', 'green', 'blue'],
                      data=[['yellow',  1.0, 1.0, 0.0],
                            ['aqua',    0.0, 1.0, 1.0],
                            ['fuchsia', 1.0, 0.0, 1.0]])
print(colors)

print('#--------')

red = colors['red']
print(red)

print('#--------')

has_red = (red == 1.0)
print(has_red)

print('#--------')

rows_with_red = colors.loc[has_red]
print(rows_with_red)

print('#--------')

print(colors.agg('mean'))

print('#--------')

print(rows_with_red.agg('mean'))

print('#--------')

print(colors.loc[colors['red'] == 1.0].agg('mean'))
