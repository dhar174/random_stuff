import os

with os.scandir('C:/') as items:
    for item in items:
        print(item.name)
