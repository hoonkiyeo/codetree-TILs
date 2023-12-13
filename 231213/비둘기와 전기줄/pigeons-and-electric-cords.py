n = int(input())
pos = []
dic = {}
for _ in range(n):
    x,y = map(int, input().split())
    pos.append((x,y))
    dic[x] = []
for x,y in pos:
    dic[x].append(y)

# val_sum = 0
# for bird in dic.keys():
#     val_sum += min(dic[bird].count(0), dic[bird].count(1))
# print(val_sum)

val_sum = 0
for key in dic.keys():
    bird = dic[key]
    cnt = 0
    if len(bird) < 2:
        continue
    for i in range(1, len(bird)):
        if bird[i] != bird[i-1]:
            cnt += 1
    val_sum += cnt
print(val_sum)