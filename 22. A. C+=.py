    no_of_test = int(input())
     
    while no_of_test > 0:
        a,b,n = map(int, input().split(" "))
        count = 0
        while max(a,b) <= n:
            if a > b:
                b += a
            else:
                a += b
            count += 1 
        print(count)        
        no_of_test -= 1
