n = int(input())
string = input()


min_length = 0

for i in range(1,n):
    lengths = []
    is_bool = True
    for j in range(n-i+1):
        consecutive_string = string[j:j+i]
        cnt = string.count(consecutive_string)
        if cnt >= 2:
            is_bool = False
    if is_bool:
        min_length = j+i - j
        break
print(min_length)