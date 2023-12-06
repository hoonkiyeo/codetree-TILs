x,y = map(int, input().split())


def interesting_num(x):
    is_bool = False
    num_list = list(set(str(x)))
    if len(num_list) == 2:
        if str(x).count(num_list[0]) == len(str(x)) - 1 or str(x).count(num_list[1]) == len(str(x)) - 1:
            is_bool =True
    return is_bool

cnt = 0
for n in range(x,y+1):
    if interesting_num(n):
        cnt += 1
print(cnt)