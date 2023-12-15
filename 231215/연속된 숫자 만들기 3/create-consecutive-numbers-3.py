pos = list(map(int, input().split()))

if pos[1] - pos[0] == 1 and pos[2] - pos[1] == 1:
    print(0)
elif pos[1] - pos[0] == 2 and pos[2] - pos[1] == 2:
    print(1)
else:
    print(max(pos[1]-pos[0], pos[2]-pos[1]) - 1)