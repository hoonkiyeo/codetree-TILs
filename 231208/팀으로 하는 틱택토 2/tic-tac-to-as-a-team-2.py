n = 3
arr = []
cnt = 0
for _ in range(3):
    n = input()
    lst = list(n)
    arr.append(lst)

coms = []
for i in range(3):
    for j in range(3):
        row = [arr[j][0], arr[j][1], arr[j][2]]
        col = [arr[0][j], arr[1][j], arr[2][j]]
        if len(set(row)) == 2:
            coms.append(sorted(row))
        if len(set(col)) == 2:
            coms.append(sorted(col))
diag_right = [arr[0][0], arr[1][1], arr[2][2]]
diag_left = [arr[0][2], arr[1][1], arr[2][0]]

if len(set(diag_right)) == 2:
    coms.append(sorted(diag_right))
if len(set(diag_left)) == 2:
    coms.append(sorted(diag_left))

new_coms = []
for com in coms:
    if com not in new_coms:
        new_coms.append(com)
print(len(new_coms))