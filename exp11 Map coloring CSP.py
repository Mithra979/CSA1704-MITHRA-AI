colors = ['Red', 'Green', 'Blue']
graph = {'A':['B'], 'B':['A','C'], 'C':['B']}
color = {}

for a in graph:
    for c in colors:
        if all(color.get(n) != c for n in graph[a]):
            color[a] = c
            break

print(color)