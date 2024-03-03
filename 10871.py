
#https://www.acmicpc.net/problem/10871

target_number = list(map(int, input().split()))
arr_number = list(map(int, input().split()))

condition = target_number[1]

for i in range(len(arr_number)):
    if arr_number[i] < condition:
        print(arr_number[i])