x = int(input())
def min_time_to_reach_greedy(X):
    time = 0
    speed = 0
    distance = 0

    while True:
        time += 1
        if distance + (speed * (speed + 1)) // 2 >= X:
            break
        distance += speed
        speed += 1

    while distance < X:
        time += 1
        distance += speed
        if distance + speed - 1 >= X:
            speed -= 1

    return time

print(min_time_to_reach_greedy(x))