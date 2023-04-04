import sys
input = sys.stdin.readline

num = int(input())
lst = []
for i in range(num):
    lst.append(input().strip())

for a,b in enumerate(lst):
    lst[a] = b.split("X")

for i in range(len(lst)):
    sum = 0
    for k in range(len(lst[i])):
        n = len(lst[i][k])
        sum += (n*(n+1))/2
    print(int(sum)) 