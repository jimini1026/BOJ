N_dct = {}

N = input()
for i in list(map(int, input().split())):
    try:
        N_dct[i] = N_dct[i] + 1
    except:
        N_dct[i] = 1

M = input()
M_lst = list(map(int, input().split()))

for i in M_lst:
    try:
        print(N_dct[i], end = " ")
    except:
        print(0, end = " ")