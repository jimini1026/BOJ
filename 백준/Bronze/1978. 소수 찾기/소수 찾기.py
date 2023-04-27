num = input()
num_lst = list(map(int, input().split()))

test_lst = []
for i in num_lst:
    test = True
    if i == 1:
        test = False
    else:
        for k in range(2,i):
            if i % k == 0:
                test = False
    if test:
        test_lst.append(i)
print(len(test_lst))