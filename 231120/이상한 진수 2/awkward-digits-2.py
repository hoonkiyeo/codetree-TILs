a = list(input())
max_a = 0

if '0' not in a:
    a[-1] = '0'
    print(int(''.join(a), 2))
else:
    for i in range(1, len(a)):
        if a[i] != '0':
            continue
        a[i] = '1'
        n = ''.join(a)
        x = int(n, 2)
        a[i] = '0'
        if x > max_a:
            max_a = x

    print(max_a)