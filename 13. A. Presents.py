    no_of_input = int(input())
    friends_seq = list(map(int, input().split(" ")))
     
    ans_seq = friends_seq.copy()
     
    for i in friends_seq:
        ans_seq[i - 1] = friends_seq.index(i)
        
        
    for i in ans_seq:
        print(i+1, end=" ")
