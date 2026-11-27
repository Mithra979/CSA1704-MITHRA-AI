room = {'A': 'Dirty', 'B': 'Dirty'}
pos = 'A'

while 'Dirty' in room.values():
    if room[pos] == 'Dirty':
        room[pos] = 'Clean'
        print(pos, "room cleaned")
    else:
        pos = 'B' if pos == 'A' else 'A'
print("All rooms are clean")