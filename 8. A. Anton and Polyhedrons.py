no_of_input = int(input())
count = 0

while no_of_input > 0:
    string_input = input()
    if string_input == "Tetrahedron":
        count += 4
    elif string_input == "Cube":
        count += 6
    elif string_input == "Octahedron":
        count += 8
    elif string_input == "Dodecahedron":
        count += 12
    elif string_input == "Icosahedron": 
        count += 20
    no_of_input -= 1

print(count)
