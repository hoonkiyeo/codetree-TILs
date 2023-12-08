n,m = map(int, input().split())
nums = list(map(int, input().split()))


def max_element_sum(n, m, sequence):
    # 누적 합을 저장할 리스트 초기화
    cumulative_sum = [0] * (n + 1)
    # 각 시작 위치에 대한 누적 합 계산
    for start in range(1, n + 1):
        position = start
        sum = 0
        for _ in range(m):
            sum += sequence[position - 1]
            position = sequence[position - 1]
        cumulative_sum[start] = sum
    # 최대 누적 합 반환
    return max(cumulative_sum)


print(max_element_sum(n,m,nums))