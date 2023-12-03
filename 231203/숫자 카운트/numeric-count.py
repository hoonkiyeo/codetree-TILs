n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def check1(n1,n2):
    n1 = str(n1)
    n2 = str(n2)
    cnt = sum(a == b for a,b in zip(n1, n2))
    return cnt

def check2(n1,n2):
    set1 = set(str(n1))
    set2 = set(str(n2))
    total = len(set1.intersection(set2))
    cnt = sum(a==b for a,b in zip(str(n1), str(n2)))
    return total - cnt

cnt = 0
for n1 in range(111, 999):
    if str(n1)[0] != str(n1)[1] != str(n1)[2]:
        is_pass = True
        for n2, a, b in arr:
            if check1(n1,n2) != a or check2(n1,n2) != b:
                is_pass = False
        if is_pass:
            cnt += 1
    continue
print(cnt)