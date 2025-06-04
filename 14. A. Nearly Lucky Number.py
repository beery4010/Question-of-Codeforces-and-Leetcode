    str_input = input()
    count = 0
    if len(str_input) == 1:
        print("NO")
    else:
        for i in str_input:
            if i in "47":
                count += 1
        if str(count) in "47":
            print("YES")
        else:
            print("NO")
