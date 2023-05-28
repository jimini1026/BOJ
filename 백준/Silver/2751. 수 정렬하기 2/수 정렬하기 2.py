import sys
input = sys.stdin.readline

num = int(input())
lst = list(map(int, [input() for _ in range(num)]))

lst.sort()

for i in lst:
    print(i)