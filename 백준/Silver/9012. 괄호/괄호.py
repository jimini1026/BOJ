import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = input().strip()
    b = ""
    while True:
        a = a.replace("()", "")
        if a == "":
            print("YES")
            break
        elif a == b:
            print("NO")
            break
        else:
            b = a