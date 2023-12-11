n = int(input())
arr = list(map(int, input().split()))

def find_sequence(n, arr):

    for i in range(1,n+1):
        for j in range(1, n+1):
            if i != j and i+j == arr[0]:
                seq = [i,j]
                used = {i,j}

                for k in range(1, n-1):
                    next_num = arr[k] - seq[-1]
                    if 1 <= next_num <= n and next_num not in used:
                        seq.append(next_num)
                        used.add(next_num)
                    else:
                        break
                if len(seq) == n:
                    return seq
    return None

for ele in find_sequence(n,arr):
    print(ele, end=' ')