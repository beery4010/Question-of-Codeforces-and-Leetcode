no_of_input = int(input())

while no_of_input > 0:
    n,k = map(int, input().split(" "))
    if n == k:
        print(str("1")*k)
    else:
        output = ["0"]*n
        step = -2
        while k > 0:
            if k == 1:
                step = 0
                output[step] = "1"
            elif k == 2:
                step = -2
                output[step] = "1"
                step = step - 1
            else:
                step = step -1
                output[step] = "1"
                    
            k -= 1
        
        print("".join(output))
        
    no_of_input -= 1
