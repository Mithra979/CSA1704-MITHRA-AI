graph = {'A': [('B', 1), ('C', 3)],
         'B': [('D', 1)], 'C': [('D', 1)], 'D': []}
h = {'A': 3, 'B': 1, 'C': 1, 'D': 0}
open_list = [(h['A'], 0, 'A')]

while open_list:
    f, g, n = open_list.pop(0)
    print(n, end=" ")
    if n == 'D':
        print("\nTotal cost:", g)
        break
    for v, cost in graph[n]:
        open_list.append((g + cost + h[v], g + cost, v))
    open_list.sort()