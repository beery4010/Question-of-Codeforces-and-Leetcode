total_cubes = int(input())
height = 0
cubes_used = 0
count = 1

while True:
    sum_of_cubes = int((count*(count + 1))/2)
    cubes_used += sum_of_cubes
    count += 1
    if cubes_used <= total_cubes:
        height += 1
    else:
        break

print(height)
