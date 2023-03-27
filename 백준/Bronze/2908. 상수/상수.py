
A, B = input().split()
reverse_a = 0
reverse_b = 0


A_list = []
for g in A:
    A_list.append(g)
A_list = list(reversed(A_list))

B_list = []
for g in B:
    B_list.append(g)
B_list = list(reversed(B_list))

for i in range(3):
    reverse_a += (10**(2-i))*int(A_list[i])

for i in range(3):
    reverse_b += (10**(2-i))*int(B_list[i])

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)