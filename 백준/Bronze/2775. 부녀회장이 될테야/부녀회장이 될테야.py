for _ in range(int(input())):
    floor = int(input())
    unit = int(input())
    lst_1 = list(range(1, unit + 1))
    
    for _ in range(floor - 1):
        lst_2 = [0] * unit
        for indx in range(unit):
            lst_2[indx] = sum(lst_1[:indx + 1])
        lst_1 = lst_2
    print(sum(lst_1))