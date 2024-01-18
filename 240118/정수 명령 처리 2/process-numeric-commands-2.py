from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        if not self.dq:
            return 1
        return 0
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        return self.dq.popleft()

    def front(self):
        return self.dq[0]

q = Queue()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        q.push(int(command[1]))
    elif command[0] == 'front':
        print(q.front())
    elif command[0] == 'size':
        print(q.size())
    elif command[0] == 'pop':
        print(q.pop())
    else:
        print(q.empty())