a = int(input())
arr_number = list(map(int, input().split()))

c = float('inf')
b = -float('inf')

for num in arr_number:
    if num < c:
        c = num
    if num > b:
        b = num

print(c, b)
