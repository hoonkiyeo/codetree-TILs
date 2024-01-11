n = int(input())
arr = list(map(int, input().split()))
k = len(str(max(arr)))

for i in range(k):    
    digit = [[] for _ in range(10)]
    for num in arr:
        digit[(num//(10**i))%10].append(num)
    numbers = []

    for d in range(10) :
        for num in digit[d] :
            numbers.append(num)
for ele in numbers:
  print(ele, end=' ')