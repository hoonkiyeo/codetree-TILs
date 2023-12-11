from itertools import combinations
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
arr2 = [x for x in range(1, n+1)]
perms = list(permutations(arr2, n))


for perm in perms:
    is_bool = True
    for i in range(n-1):
        if perm[i] + perm[i+1] != arr[i]:
            is_bool = False
    if is_bool:
        break

for ele in perm:
    print(ele, end=' ')