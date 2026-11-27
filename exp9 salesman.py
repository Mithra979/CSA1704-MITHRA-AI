from itertools import permutations

d = [[0, 10, 15, 20],
     [10, 0, 35, 25],
     [15, 35, 0, 30],
     [20, 25, 30, 0]]
best = 999
for p in permutations([1, 2, 3]):
    route = (0,) + p + (0,)
    cost = sum(d[route[i]][route[i+1]] for i in range(4))
    if cost < best:
        best, path = cost, route
print("Shortest route:", path)
print("Minimum cost:", best)