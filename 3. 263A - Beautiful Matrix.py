    no_of_input = 5
    matrix = []
     
    while no_of_input > 0:
        row = list(map(int, input().split(" ")))
        matrix.append(row)
        no_of_input -= 1
     
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                row_index = i
                col_index = j
                break
     
    # Manhattan Distance = |x1 - x2| + |y1 - y2| -> for center (2,2)
    dist = abs(row_index - 2) + abs(col_index - 2)
     
    print(dist)
