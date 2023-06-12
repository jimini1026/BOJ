M = int(input())
M_list = sorted(input().split())
N = int(input())
N_list = input().split()

for i in N_list:
    start = 0
    end = M - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if i == M_list[mid]:
            print(1)
            found = True
            break
        elif i > M_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not found:
        print(0)