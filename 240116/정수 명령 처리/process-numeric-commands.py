class Stack:
    def __init__(self):          # 빈 스택 하나를 생성합니다.
        self.items = []
                
    def push(self, item):        # 스택에 데이터를 추가합니다.
        self.items.append(item)
                
    def empty(self):             # 스택이 비어있으면 True를 반환합니다.
        if not self.items:
            return 1
        return 0
                
    def size(self):              # 스택에 있는 데이터 수를 반환합니다.
        return len(self.items)
        
    def pop(self):               # 스택의 가장 위에 있는 데이터를 반환하고 제거합니다.
        return self.items.pop()
                
    def top(self):               # 스택의 가장 위에 있는 데이터를 제거하지 않고 반환합니다.                        
        return self.items[-1]

s = Stack()
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(int(command[1]))
    elif command[0] == 'pop':
        print(s.pop())
    elif command[0] == 'empty':
        print(s.empty())
    elif command[0] == 'top':
        print(s.top())
    elif command[0] == 'size':
        print(s.size())