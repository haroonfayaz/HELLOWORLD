a = round(4.576)
b = round(4.43)
print(f' {a}, {b},{type(a)}')


colors = ['Red', 'Blue', 'Green']
objects = ['Car', 'Pen', 'Grass']

z = zip(colors, objects)
for x in z:
    print(x[0] + " " + x[1])
