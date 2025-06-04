no_of_input = int(input())
no_of_pas = []
total_pass = 0

while no_of_input > 0:
    enter, exit = map(int, input().split(" "))
    total_pass = exit - enter + total_pass
    no_of_pas.append(total_pass)
    no_of_input -= 1

print(max(no_of_pas))
