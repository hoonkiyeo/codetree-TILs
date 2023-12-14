a,b,x,y = map(int, input().split())

# a -> b 직행
dist1 = abs(b-a)

# a -> x -> y -> b
dist2 = abs(x-a) + abs(y-b)

# a -> y -> x -> b
dist3 = abs(y-a) + abs(b-x)

min_dist = min(dist1, dist2, dist3)
print(min_dist)