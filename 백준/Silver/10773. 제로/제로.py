lst = []

for _ in range(int(input())):
    num = int(input())
    if num == 0: del lst[-1]
    else: lst.append(num)

print(sum(lst))