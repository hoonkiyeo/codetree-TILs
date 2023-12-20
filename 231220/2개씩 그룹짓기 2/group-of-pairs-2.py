n = int(input())
nums = list(map(int, input().split()))
def max_min_difference_corrected(n, numbers):
    # 정렬
    numbers.sort()

    # 인접한 원소들의 차이 계산
    differences = [abs(numbers[i] - numbers[i + 1]) for i in range(0, 2 * n - 1, 2)]

    # 최댓값 반환 (최솟값의 최댓값을 찾기 위함)
    return max(differences)


print(max_min_difference_corrected(n,nums))