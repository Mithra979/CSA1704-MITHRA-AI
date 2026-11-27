b = [' '] * 9

for i in range(9):
    print(b[0:3], b[3:6], b[6:9])
    p = 'X' if i % 2 == 0 else 'O'
    n = int(input(p + " position (0-8): "))
    b[n] = p
    if any(all(b[j] == p for j in line) for line in
    [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]):
        print(p, "wins!")
        break
else:
    print("Draw!")