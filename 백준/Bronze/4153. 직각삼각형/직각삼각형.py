while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    else:
        lst = [a, b, c]
        lst.sort()
        if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2:
            print("right")
        else:
            print("wrong")