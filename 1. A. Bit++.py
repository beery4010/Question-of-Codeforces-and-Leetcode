no_of_input = int(input())
count = 0

while no_of_input > 0:
    character = input()
    if (character == "X++") or (character == "++X"):
        count += 1
    elif (character == "X--") or (character == "--X"):
        count -= 1
    no_of_input -= 1
print(count)
