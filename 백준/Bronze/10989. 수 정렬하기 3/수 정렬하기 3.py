import sys
input = sys.stdin.readline

num = int(input())
lst = [0]*10001

for _ in range(num):
    value = int(input())
    lst[value] += 1

location = -1
for i in lst:
    location += 1
    if i != 0:
        for _ in range(i):
            print(location)