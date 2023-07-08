L = int(input())
num = 0
for i, alphabet in enumerate(input()):
    num += (ord(alphabet) - 96) * (31 ** i)

M = 1234567891

if num >= M:
    num = num % M
print(num)