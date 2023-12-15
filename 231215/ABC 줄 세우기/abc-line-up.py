n = int(input())
arr = list(input().split())
target_arr = sorted(arr)
cnt = 0

while True:
    if arr == target_arr:
        break   
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt += 1
print(cnt)
        
# B C A
# B A C
# A B C


# B D C A
# B C D A
# B C A D
# B A C D
# A B C D


# B D C A
# B D A C
# B A D C
# A B D C
# A B C D


# D C A E B
# C D A E B
# C A D E B
# C A D B E
# A C D B E
# A C B D E
# A B C D E