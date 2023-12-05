n, m, d, s = map(int, input().split())
arr_cheese = [tuple(map(int, input().split())) for _ in range(d)]
arr_sick = sorted([tuple(map(int, input().split())) for _ in range(s)])

set_arr = [] # 아픈 사람들이 아프기 전 먹은 치즈 기록하는 set
sick_people_set = set() # 아픈 사람이 누구인지 기록하는 set

for i in range(len(arr_sick)):
    sick_person = arr_sick[i][0]
    time = arr_sick[i][1]
    sick_people_set.add(sick_person)
    arr_bad_cheese = set()
    for c in arr_cheese:
        if c[0] == sick_person and c[2] < time:
            arr_bad_cheese.add(c[1])
    set_arr.append(arr_bad_cheese)

bad_cheeses = set_arr[0]
for s in set_arr:
    bad_cheeses = bad_cheeses & s

for p,x,t in arr_cheese:
    if x in bad_cheeses:
        sick_people_set.add(p)
print(len(sick_people_set))