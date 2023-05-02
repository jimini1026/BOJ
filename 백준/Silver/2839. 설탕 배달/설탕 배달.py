total = int(input())

lst_a = []
lst_b = []

for i in range(int((total / 3) + 1)):
    if i != 0:
        test_a = i
        test_b = int((total - 3 * i) / 5)
    else:
        test_a = 0
        test_b = int(total / 5)
    lst_a.append(test_a)
    lst_b.append(test_b)

value = []
for i in range(len(lst_a)):
    if (3 * lst_a[i]) + (5 * lst_b[i]) == total:
        value.append([lst_a[i], lst_b[i]])

num = 2000
if len(value) > 0:
    for i in value:
        price = i[0]+i[1]
        if price < num:
            num = price
else:
    num = -1

print(num)