    no_of_input = int(input())
    height = list(map(int, input().split(" ")))
     
    moves = height.index(max(height)) + height[::-1].index(min(height))
    if height.index(max(height)) > (no_of_input - 1 - height[::-1].index(min(height))):
        moves -= 1
     
    print(moves)
