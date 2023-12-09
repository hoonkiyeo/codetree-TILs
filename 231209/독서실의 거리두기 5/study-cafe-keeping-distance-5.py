n = int(input())
seats = [*input()]

max_dist = 0
for i in range(n):
    dist = 0
    dist1 = 0
    dist2 = 0
    pos = 0
    if seats[i] == '0':
        pos = i
        arr1 = seats[i:]
        arr2 = seats[:i+1][::-1]
        
        if '1' in arr1:
            dist1 = arr1.index('1')
        else:
            dist1 = len(arr1) - 1
        if '1' in arr2:
            dist2 = arr2.index('1')
        else:
            dist2 = len(arr2) - 1
        dist = min(dist1, dist2)
    max_dist = max(dist, max_dist)
print(max_dist)