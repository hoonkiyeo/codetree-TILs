def calculate_h_score(sequence):
    sequence.sort(reverse=True)
    h_score = 0
    for i, num in enumerate(sequence):
        if i + 1 >= num:
            h_score = max(h_score, num)
    return h_score

def max_h_score(N, L, sequence):
    frequency = {}
    for num in sequence:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # 빈도수에 따라 정렬
    sorted_nums = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    for num, freq in sorted_nums:
        if L <= 0:
            break
        increase = min(L, freq)
        L -= increase
        for i in range(len(sequence)):
            if sequence[i] == num:
                sequence[i] += 1
                increase -= 1
                if increase == 0:
                    break

    return calculate_h_score(sequence)

def main():
    N, L = map(int, input().split())
    sequence = list(map(int, input().split()))
    print(max_h_score(N, L, sequence))

if __name__ == "__main__":
    main()