N = int(input())

value = 0
test = 1

while (N - test) > 0:
    value += 1
    test += 6 * value

print(value+1)