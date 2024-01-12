n = int(input())
arr = list(map(int, input().split()))
merged_arr = [0] * n

def mergesort(arr, low, high):
    if low < high:
        mid = (low+high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(low, mid, high)

def merge(low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
            k += 1
    
    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        merged_arr[k] = arr[j]
        k += 1
        j += 1
    
    for l in range(low, high+1):
        arr[l] = merged_arr[l]
    

mergesort(arr, 0, n-1)
print(*arr)