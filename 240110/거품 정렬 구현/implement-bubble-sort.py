n = int(input())
arr = list(map(int, input().split()))

while True:
    if arr == sorted(arr):
        break
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp

for ele in arr:
    print(ele, end=' ')