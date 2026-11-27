from collections import deque

def jug():
    q = deque([(0, 0)]); seen = set()
    while q:
        a, b = q.popleft()
        if (a, b) in seen: continue
        seen.add((a, b)); print(a, b)
        if a == 2: print("Goal Reached"); return
        for x in [(4,b),(a,3),(0,b),(a,0),(max(0,a-3+b),min(3,a+b)),
                  (min(4,a+b),max(0,b-4+a))]: q.append(x)

jug()