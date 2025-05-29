x1, x2, x3 = map(int, input().split(" "))

sorted_lst = sorted([x1,x2,x3])

center = sorted_lst[1]

dist = abs(sorted_lst[0] - center) + abs(sorted_lst[2] - center)

print(dist)
