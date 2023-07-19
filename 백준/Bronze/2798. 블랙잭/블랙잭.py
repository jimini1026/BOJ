N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0
for indx_1, i in enumerate(card):
    for indx_2, j in enumerate(card[indx_1 + 1:], indx_1 + 1):
        for k in card[indx_2 + 1:]:
            sum = i + j + k
            if sum <= M:
                result = max(result, sum)
print(result)