N,X = map(int,input().split())

list = list(map(int,input().split()))

value = []
for i in list:
    if i < X:
        value.append(i)

print(*value)