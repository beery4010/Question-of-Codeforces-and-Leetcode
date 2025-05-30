no_of_input = int(input())
prob = list(map(int, input().split(" ")))

max_value = max(prob)

if max_value == 1:
    print("Hard")
else:
    print("Easy")
