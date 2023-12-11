def calculate_h_score(sequence):
    sequence.sort(reverse=True)
    h_score = 0
    for i in range(len(sequence)):
        if sequence[i] >= i + 1:
            h_score = i + 1
    return h_score

def max_h_score(N, L, sequence):
    original_h_score = calculate_h_score(sequence)
    if L == 0:
        return original_h_score

    for _ in range(L):
        sequence.sort(reverse=True)
        for i in range(len(sequence)):
            if i == 0 or sequence[i] != sequence[i - 1]:
                sequence[i] += 1
                break

    return max(original_h_score, calculate_h_score(sequence))

def main():
    N, L = map(int, input().split())
    sequence = list(map(int, input().split()))
    print(max_h_score(N, L, sequence))

if __name__ == "__main__":
    main()