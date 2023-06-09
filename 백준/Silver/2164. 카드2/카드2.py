card = int(input())
lst = [""] * (card + (card - 1))

for i in range(1, card + 1):
    lst[i - 1] = i

indx = 1
len_lst = card
for _ in range(card - 1):
    lst[len_lst] = lst[indx]
    indx += 2
    len_lst += 1
print(lst[-1])