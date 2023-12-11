from itertools import combinations
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
arr2 = [x for x in range(1, n+1)]
perms = list(permutations(arr2, n))

for perm in perms:
    ans = []
    for i in range(n-1):
        ans.append(perm[i] + perm[i+1])
    if ans == arr:
        break

for ele in perm:
    print(ele, end=' ')