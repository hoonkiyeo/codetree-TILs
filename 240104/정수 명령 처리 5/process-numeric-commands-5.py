n = int(input())
arr = []
for i in range(n):
    x = input().split()
    if x[0] == 'push_back':
        arr.append(int(x[1]))
    elif x[0] == 'pop_back':
        arr.pop(-1)
    elif x[0] == 'size':
        print(len(arr))
    elif x[0] == 'get':
        print(arr[int(x[1])-1])