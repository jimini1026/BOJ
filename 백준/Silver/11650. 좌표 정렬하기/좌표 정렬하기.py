N = int(input())
lst = [0] * N

for indx in range(N):
    lst[indx] = list(map(int, input().split()))

lst.sort(key = lambda y: y[1])
lst.sort(key = lambda x: x[0])

for i in lst:
    print(*i)