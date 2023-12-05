x,y = map(int, input().split())

max_sum = 0
for n in range(x,y+1):
    units = int(str(n // 1)[-1])
    tens = int(str(n // 10)[-1])
    hundreds = int(str(n // 100)[-1])
    thousands = int(str(n // 1000)[-1])
    ten_thousands = int(str(n // 10000)[-1])
    total_sum = units + tens + hundreds + thousands + ten_thousands
    max_sum = max(max_sum, total_sum)
print(max_sum)