k,n,w = map(int, input().split(" "))

cost_amount = 0

for i in range(w):
    cost_amount += (i+1)*k
    
req_amount = cost_amount - n

if req_amount > 0:
    print(req_amount)
else:
    print(0)
