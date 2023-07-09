N, M = map(int, input().split())
lst = list(range(1, N + 1))

for _ in range(M):
    change_1, change_2 = map(int, input().split())
    lst[change_1 - 1], lst[change_2 - 1] = lst[change_2 - 1], lst[change_1 - 1]
print(*lst)
