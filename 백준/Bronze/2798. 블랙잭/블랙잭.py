N, M = map(int, input().split())
card = list(map(int, input().split()))

lst = []
for indx_1, i in enumerate(card):
    for indx_2, j in enumerate(card[indx_1 + 1:], indx_1 + 1):
        for k in card[indx_2 + 1:]:
            lst.append(i + j + k)

lst.sort()

for indx, i in enumerate(lst, 1):
    if i > M:
        break
    else:
        num = i

print(num)