S = list(input())

from string import ascii_lowercase

alphabet = {}

for i in ascii_lowercase:
    alphabet[i] = -1

for k in S:
    alphabet[k] = S.index(k)

for j in alphabet.values():
    print(j, end = " ")