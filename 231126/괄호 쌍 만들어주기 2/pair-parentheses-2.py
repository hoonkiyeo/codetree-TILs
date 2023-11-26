s = input()

open_ = 0
close_ = 0
idx = 0
for i in range(len(s)-1):
    if s[i] == '(' and s[i+1] == '(':
        idx = i+1
        break
for i in range(len(s)-1):
    if s[i] == '(' and s[i+1] == '(':
        open_ += 1
for i in range(idx, len(s)-1):
    if s[i] == ')' and s[i+1] == ')':
        close_ += 1
print(open_ + close_)