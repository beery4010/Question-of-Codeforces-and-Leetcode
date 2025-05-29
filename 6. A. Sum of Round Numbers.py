no_of_input = int(input())
ans = []

while no_of_input > 0:
    num = int(input())
    i = 10
    n = 0
    string = ""
    if len(str(num)) == 1:
        ans.append(len(str(num)))
        ans.append(num)
    else: 
        count = 0
        while n < len(str(num)):
            n += 1
            rem = num % i
            i *= 10
            num -= rem
            if rem == 0:
                continue
            else: 
                count += 1
                string = string + str(rem) + " "
        ans.append(count)
        ans.append(string)
    no_of_input -= 1
    
for i in ans:
    print(i)
