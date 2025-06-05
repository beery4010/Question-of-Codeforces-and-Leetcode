table_card = input()
cards_on_table = list(input())
count = 0

for i in cards_on_table:
    if i in table_card:
        count += 1

if count > 0:
    print("YES")
else:
    print("NO")
