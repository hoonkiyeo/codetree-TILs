n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sum(arr)
for i in range(max(arr), sum(arr)+1):
    # max(arr): 설정할 수 있는 minimax
    # sum(arr): 최대로 설정할 수 있는 최댓값

    section = 1
    cnt = 0

    # 만약 현재값 + 다음값 > 설정한 최댓값: 현재 구간 종료 및 새로운 구간 시작
    for j in range(n):
        if cnt + arr[j] > i:
            cnt = 0
            section += 1
        cnt += arr[j]

    # 총 구간의 수가 m보다 작거나 같을 경우에만 가능
    if section <= m:
        ans = min(ans, i)
print(ans)