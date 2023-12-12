n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    indices = [0]
    for i in range(1,n):
        if arr[i] <= max_val:
            indices.append(i)
    for i in range(len(indices)-1):
        if indices[i+1] - indices[i] > k:
            return False
    return True

for i in range(max(arr[0], arr[n-1]), 101):
    if is_possible(i):
        print(i)
        break