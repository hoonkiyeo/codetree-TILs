arr = []
for _ in range(19):
    arr.append(list(map(int, input().split())))

black = 0
white = 0
is_black = False
is_white = False
idx_b = [0,0]
idx_w = [0,0]

def check_black(arr,x,y):
    if arr[x][y] == 1:
        return True
    return False
def check_white(arr,x,y):
    if arr[x][y] == 2:
        return True
    return False

for i in range(19):
    for j in range(19):
        if arr[i][j] == 1: # black
            if check_black(arr, i, j+1) and check_black(arr, i, j+2) and check_black(arr, i, j+3) and check_black(arr, i, j+4):
                idx_b = [i,j+2]
                is_black = True
                break
            elif check_black(arr, i+1, j) and check_black(arr, i+2, j) and check_black(arr, i+3, j) and check_black(arr, i+4, j):
                idx_b = [i+2,j]
                is_black = True
                break
            elif check_black(arr, i+1, j+1) and check_black(arr, i+2, j+2) and check_black(arr, i+3, j+3) and check_black(arr, i+4, j+4):
                idx_b = [i+2, j+2]
                is_black = True
                break
        elif arr[i][j] == 2: # white
            if check_white(arr, i, j+1) and check_white(arr, i, j+2) and check_white(arr, i, j+3) and check_white(arr, i, j+4):
                idx_w = [i,j+2]
                is_white = True
                break
            elif check_white(arr, i+1, j) and check_white(arr, i+2, j) and check_white(arr, i+3, j) and check_white(arr, i+4, j):
                idx_w = [i+2,j]
                is_white = True
                break
            elif check_white(arr, i+1, j+1) and check_white(arr, i+2, j+2) and check_white(arr, i+3, j+3) and check_white(arr, i+4, j+4):
                idx_w = [i+2, j+2]
                is_white = True
                break

if is_black:
    print(1)
    print(idx_b[0]+1, idx_b[1]+1)
elif is_white:
    print(2)
    print(idx_w[0]+1, idx_w[1]+1)
else:
    print(0)