N = int(input())
lst = [0] * N

for indx in range(N):
    lst[indx] = list(map(int, input().split()))

lst.sort(key = lambda x: (x[0], x[1]))

for i in lst:
    print(*i)