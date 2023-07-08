L = int(input())
num = 0
for i, alphabet in enumerate(input()):
    num += (ord(alphabet) - 96) * (31 ** i)
print(num % 1234567891)