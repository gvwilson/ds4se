import sys

print('Lines,Characters,Path')
for line in sys.stdin:
    fields = line.split()
    print('{},{},{}'.format(*fields))
