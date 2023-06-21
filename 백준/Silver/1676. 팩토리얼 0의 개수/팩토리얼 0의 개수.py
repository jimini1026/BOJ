N = int(input())

fact = 1
for i in range(1, N + 1):
    fact *= i

count = 0
for i in str(fact)[::-1]:
    if i == "0":
        count += 1
    else:
        break
print(count)