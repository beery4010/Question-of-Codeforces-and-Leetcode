no_of_input = int(input())
list_of_apartment_no = []

for num in range(1,10):
    count = str(num)
    for i in range(1,5):
        str_num = i*count
        list_of_apartment_no.append(str_num)
        
while no_of_input > 0:
    floor_no = input()
    total_digit = 0
    for i in list_of_apartment_no:
        if floor_no == i:
            total_digit += len(i)
            print(total_digit)
            break
        else: 
            total_digit += len(i)
    no_of_input -= 1
