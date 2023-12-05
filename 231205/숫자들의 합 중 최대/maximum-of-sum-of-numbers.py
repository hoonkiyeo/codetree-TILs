x,y = map(int, input().split())



max_sum = 0
for i in range(x,y+1):
    total_sum = (i % 10) + (i // 10) + (i // 100) + (i // 1000) + (i // 10000)
    max_sum = max(max_sum, total_sum)
print(max_sum)