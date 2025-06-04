num, times = map(int, input().split(" "))

while times > 0:
    if num % 10 == 0:
        num = int(num/10)
    else:
        num -= 1
    times -= 1

print(num)
