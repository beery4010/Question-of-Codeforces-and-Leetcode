no_of_input = int(input())
     
while no_of_input > 0:
    n,x = map(int, input().split(" "))
    doors_str = input()
    first = doors_str.find("1")
    last = doors_str.rfind("1")
    lst = doors_str[first:last+1].replace(" ","")
    if len(lst) <= x:
        print("Yes")
    else:
        print("No")
    no_of_input -= 1
