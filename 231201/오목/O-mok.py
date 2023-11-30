arr = []
for _ in range(19):
    arr.append(list(map(int, input().split())))

def is_winner(arr, player):
    for i in range(19):
        for j in range(19):
            if arr[i][j] == player:
                # Check horizontally
                if j <= 14 and all(arr[i][j + k] == player for k in range(1, 5)):
                    return True, [i + 1, j + 3]
                # Check vertically
                if i <= 14 and all(arr[i + k][j] == player for k in range(1, 5)):
                    return True, [i + 3, j + 1]
                # Check diagonal down-right
                if i <= 14 and j <= 14 and all(arr[i + k][j + k] == player for k in range(1, 5)):
                    return True, [i + 3, j + 3]
                # Check diagonal up-right
                if i >= 4 and j <= 14 and all(arr[i - k][j + k] == player for k in range(1, 5)):
                    return True, [i - 1, j + 3]
    return False, []

is_black, black_idx = is_winner(arr, 1)
is_white, white_idx = is_winner(arr, 2)

if is_black:
    print(1)
    print(*black_idx)
elif is_white:
    print(2)
    print(*white_idx)
else:
    print(0)