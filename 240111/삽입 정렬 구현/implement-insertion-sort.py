n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    j = i - 1
    key = arr[i]

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1    
    arr[j+1] = key

for ele in arr:
    print(ele, end=' ')