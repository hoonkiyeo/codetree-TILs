# function radix_sort(arr, k)
#   for pos = k - 1 ... pos >= 0:
#     set arr_new = [10][]
#     for i = 0 ... i < arr.size
#       set digit = posth digit of arr[i]
#       arr_new[digit].append(arr[i])

#     set store_arr = []
#     for i = 0 ... i < 10
#       for j = 0 ... j < arr_new[i].size
#         store_arr.append(arr_new[i][j])
  
#     arr = store_arr

#   return arr

n = int(input())
arr = list(map(int, input().split()))
k = len(str(max(arr)))

for pos in range(k)[::-1]:
  arr_new = [[0] for _ in range(10)]
  for i in range(n):
    digit = int(str(arr[i])[pos])
    arr_new[digit].append(arr[i])
  
  store_arr = []
  for i in range(10):
    for j in range(len(arr_new[i])):
      store_arr.append(arr_new[i][j])
  
  arr = store_arr

for ele in arr:
  if ele > 0:
    print(ele, end=' ')