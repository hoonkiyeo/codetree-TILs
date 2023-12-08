n = int(input())
string = input()


def find_string(s, target):
    cnt = 0
    for i in range(len(s)):
        if s[i:i+len(target)] == target:
            cnt += 1
    return cnt

min_length = 0
for i in range(1,n):
    is_bool = True
    for j in range(n-i+1):
        target_string = string[j:j+i]
        cnt = find_string(string, target_string)
        if cnt >= 2:
            is_bool = False
    if is_bool:
        min_length = len(target_string)
        break
print(min_length)