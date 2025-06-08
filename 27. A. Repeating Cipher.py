length = int(input())
repeating_str = list(input())
index = 0
count = 1
simple_str = ""

while index < length:
    simple_str = simple_str + repeating_str[index]
    index = int((count * (count+1))/2)
    count += 1
    
print(simple_str)
