no_of_input = int(input())

while no_of_input > 0:
    num = input()
    if "1" not in num:
        print(0)
        no_of_input -= 1
        continue
    first = num.find("1")
    last = num.rfind("1")
    count = num[first: last+1].count("0")
    print(count)
    no_of_input -= 1
