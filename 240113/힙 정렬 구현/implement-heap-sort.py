def max_heapify(arr, n, i):
    largest = i  # 부모 노드의 인덱스로 초기화
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스

    # 왼쪽 자식 노드가 부모 노드보다 크면 largest 값을 갱신
    if left < n and arr[largest] < arr[left]:
        largest = left

    # 오른쪽 자식 노드가 부모 노드보다 크면 largest 값을 갱신
    if right < n and arr[largest] < arr[right]:
        largest = right

    # largest 값이 갱신되었다면 노드를 교환하고, 재귀적으로 Max Heapify를 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# 힙 정렬 함수
def heap_sort(arr):
    n = len(arr)

    # 입력 배열을 최대 힙 형태로 만듦
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # 힙에서 최대 원소를 추출하고 정렬된 부분에 추가
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최대 원소를 맨 뒤로 이동
        max_heapify(arr, i, 0)  # 힙 속성 유지

    return arr

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = heap_sort(arr)
print(*sorted_arr)