A=int(input())
B=int(input())
C=int(input())

num = A * B * C
list = []
for i in str(num):
    list.append(int(i))
dict = {}

for e in range(10):
    dict[e] = 0

for g in list:
    if g in dict:
        dict[g] += 1

for h in dict.values():
    print(h)