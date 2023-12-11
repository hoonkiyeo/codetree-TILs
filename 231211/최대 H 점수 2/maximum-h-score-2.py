from collections import Counter

def calculate_h_score(sequence):
    sequence.sort(reverse=True)
    h_score = 0
    for i, num in enumerate(sequence):
        if i + 1 >= num:
            h_score = max(h_score, num)
    return h_score

def max_h_score(N, L, sequence):
    count = Counter(sequence)
    most_common = count.most_common()

    for num, freq in most_common:
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