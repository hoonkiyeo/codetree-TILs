from itertools import permutations
arr = list(map(int, input().split()))
n = len(arr)

def find_solution(arr):
    for p in permutations(arr, 4):
        a,b,c,d = sorted(p)

        if all(x in arr for x in [a,b,c,d,a+b,a+c,a+d,b+c,b+d,c+d,a+b+c,a+b+d,b+c+d,a+b+c+d]):
            return a,b,c,d
    return 'No solution'

for i in find_solution(arr):
    print(i, end=' ')