n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split()) 
    coords.append((x,y))

max_area = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1,y1 = coords[i]
            x2,y2 = coords[j] 
            x3,y3 = coords[k]
            if (x1 == x2 and y2 == y3) or (x1 == x3 and y3 == y2) or \
               (x2 == x3 and y3 == y1) or (x2 == x1 and y1 == y3) or \
               (x3 == x1 and y1 == y2) or (x3 == x2 and y2 == y1):
                area = 1/2*abs((x1*x2 + x2*y3 + x3*y1) - (x2*y2 + x3*y2 + x1*y3))
                max_area = max(max_area, area)
print(int(max_area * 2))