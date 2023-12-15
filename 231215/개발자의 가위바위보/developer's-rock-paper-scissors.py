n = int(input())
matches = []
for _ in range(n):
    x,y = map(int, input().split())
    matches.append((x,y))
win_cnt = 0

# case1: 1=가위, 2=바위, 3=보
# case2: 1=가위, 2=보, 3=바위
cnt1 = 0
cnt2 = 0
for i in range(n):
    x,y = matches[i]
    if x == 1:
        if y == 3:
            cnt1 += 1
        elif y == 2:
            cnt2 += 1
    elif x == 2:
        if y == 1:
            cnt1 += 1
        elif y == 3:
            cnt1 += 1
    elif x == 3:
        if y == 2:
            cnt1 += 1
        elif y == 1:
            cnt2 += 1
# case3: 1=바위, 2=보, 3=가위
# case4: 1=바위, 2=가위, 3=보
cnt3 = 0
cnt4 = 0
for i in range(n):
    x,y = matches[i]
    if x == 1:
        if y == 3:
            cnt3 += 1
        elif y == 2:
            cnt4 += 1
    elif x == 2:
        if y == 1:
            cnt3 += 1
        elif y == 3:
            cnt4 += 1
    elif x == 3:
        if y == 2:
            cnt3 += 1
        elif y == 1:
            cnt4 += 1
# case5: 1=보, 2=바위, 3=가위
# case6 = 1=보, 2=가위, 3=바위
cnt5 = 0
cnt6 = 0
for i in range(n):
    x,y = matches[i]
    if x == 1:
        if y == 2:
            cnt5 += 1
        elif y == 3:
            cnt6 += 1
    elif x == 2:
        if y == 3:
            cnt5 += 1
        elif y == 1:
            cnt6 += 1
    elif x == 3:
        if y == 1:
            cnt5 += 1
        elif y == 2:
            cnt6 += 1

win_cnt = max(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6)
print(win_cnt)