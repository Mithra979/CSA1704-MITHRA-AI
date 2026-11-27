from collections import deque

def bfs(start, goal):
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path + [state]

        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new = list(state)
                i = nr * 3 + nc
                new[z], new[i] = new[i], new[z]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [state]))

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = bfs(start, goal)

print("Solution:")
for s in solution:
    print(s[:3])
    print(s[3:6])
    print(s[6:])
    print()