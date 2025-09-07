import pandas as pd

example = pd.DataFrame(data=[[  1,   2,   3],
                             [ 10,  20,  30],
                             [100, 200, 300]],
                       columns=['left', 'middle', 'right'])
print(example)

print('#--------')

print(example['left'] + example['middle'])

print('#--------')

print(5 * example['left'])

print('#--------')

print(example.agg('sum'))

print('#--------')

print(example.agg(['sum', 'mean']))
