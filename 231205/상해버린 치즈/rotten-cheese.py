# n: 사람의 수
# m: 치즈의 수
# d: 먹은 기록의 수
# s: 아픈 기록의 수
N,M,D,S = map(int,input().split())

arr = []
for _ in range(D):
    p,m,t = map(int, input().split())
    # p: 몇번 째 사람
    # m: 몇 번째 치즈
    # t: 먹은 시점 (초)
    arr.append((p,m,t))

sick = []
sick_p = []
sick_cnt = 0
for _ in range(S):
    p,t = map(int,input().split())
    # p: 아팠던 사람
    # t: 아팠던 시점
    sick.append((p,t))
    sick_p.append(p)
    sick_cnt += 1

bad_cheese = [0] * (M+1)
final_cheese = []
for i in range(len(sick)):
    person = sick[i][0]
    time = sick[i][1]
    for j in range(len(arr)):
        person2 = arr[j][0]
        cheese = arr[j][1]
        time2 = arr[j][2]
        if person == person2:
            if time2 < time:
                bad_cheese[cheese] += 1
for i in range(len(bad_cheese)):
    if bad_cheese[i] >= sick_cnt:
        final_cheese.append(i)

sick_cnt2 = 0
for i in range(len(arr)):
    p,m,t = arr[i][0], arr[i][1], arr[i][2]
    if p in sick_p:
        continue
    if m in final_cheese:
        sick_cnt2 += 1

print(sick_cnt + sick_cnt2)