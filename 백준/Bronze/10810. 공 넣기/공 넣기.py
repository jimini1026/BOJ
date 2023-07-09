N, M = map(int, input().split())
lst = [0] * N

for _ in range(M):
    start, end, ball = map(int, input().split())
    for i in range(start - 1, end):
        lst[i] = ball
print(*lst)