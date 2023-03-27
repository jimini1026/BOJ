text = input().upper()
dict = {}
for i in text:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

alphabet = list(dict.keys())
frequency = list(dict.values())

for i in range(len(alphabet)):
    if max(frequency) == frequency[i]:
        index=i

test=0
for i in range(len(alphabet)):
    if frequency[index] == frequency[i]:
        test += 1
if test>=2:
    print("?")
else:
    print(alphabet[index])
