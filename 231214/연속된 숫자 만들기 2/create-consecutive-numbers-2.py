arr = list(map(int, input().split()))

if arr[1] - arr[0] == 2 or arr[2] - arr[1] == 2:
    print(1)
else:
    print(2)