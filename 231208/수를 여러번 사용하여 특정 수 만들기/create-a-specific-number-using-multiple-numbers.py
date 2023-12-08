a,b,c = map(int, input().split())
threshold = 1000

max_val = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        val = (a*i) + (b*j)
        if val <= c:
            max_val = max(max_val, val)
print(max_val)