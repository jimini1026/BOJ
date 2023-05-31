lst = []

for _ in range(int(input())):
    lst.append(input().split())
lst.sort(key = lambda x: int(x[0]))

for age, name in lst:
    print(int(age), name)