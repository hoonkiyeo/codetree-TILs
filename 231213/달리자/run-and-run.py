n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_dist = 0
for i in range(n):
    if A[i] > B[i]:
        diff = A[i] - B[i]
        A[i] -= diff
        A[i+1] += diff
        total_dist += diff
print(total_dist)