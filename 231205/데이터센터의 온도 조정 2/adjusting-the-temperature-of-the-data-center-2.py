n,c,g,h = map(int, input().split())
temps = []

for _ in range(n):
    ta,tb = map(int, input().split())
    temps.append((ta,tb))

max_resource = 0
for i in range(1,1001):
    resource = 0
    for ta,tb in temps:
        if i < ta:
            resource += c
        elif ta <= i <= tb:
            resource += g
        elif i > tb:
            resource += h
    max_resource = max(max_resource, resource)
print(max_resource)