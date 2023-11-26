import sys
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

min_dist = sys.maxsize
for i in range(len(lst)):
    dist = 0
    for j in range(len(lst)):
        dist += lst[j] * j
    if dist < min_dist:
        min_dist = dist
    lst = lst[1:] + lst[:1]
print(min_dist)