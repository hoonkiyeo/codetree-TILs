n,m = map(int, input().split())
pos = list(map(int, input().split()))
wifi_range = 2*m+1
cnt = 0

# for i in range(0, n, wifi_range):
#     if 1 in pos[i:i+(wifi_range)]:

#         check_list = pos[i:(i+(wifi_range))*2]
#         print(check_list)

# 0 0 1 1 0 0
# 0 1 1 1 0 0
# 0 0 1 1 1 0

def min_wifi(n, m, houses):
    i = 0
    wifi_count = 0

    while i < n:
        if houses[i] == 1:
            # 와이파이를 설치할 위치 찾기
            wifi_pos = min(i + m, n - 1)
            wifi_count += 1

            # 와이파이가 커버하는 마지막 위치 찾기
            i = wifi_pos + m + 1
        else:
            i += 1

    return wifi_count
print(min_wifi(n,m,pos))