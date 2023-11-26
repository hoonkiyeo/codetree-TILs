s = input()

open_ = 0
close_ = 0
idx = []
for i in range(len(s)-1):
    if s[i] == '(' and s[i+1] == '(':
        open_ += 1
        idx.append(i+1)

for i in idx:
    for j in range(i, len(s)-1):
        if s[j] == ')' and s[j+1] == ')':
            close_ += 1

print(close_)