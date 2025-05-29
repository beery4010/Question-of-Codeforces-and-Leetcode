n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink_ml = k*l
total_shot_ml = int(total_drink_ml/nl)

total_lime = c*d

total_salt = int(p/np)

print(int(min(total_shot_ml, total_lime, total_salt)/n))
