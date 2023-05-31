import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))

for each_lst in lst:
    guest_num = each_lst[2]
    floor = guest_num % each_lst[0]
    room = (guest_num // each_lst[0])+ 1
    
    if guest_num % each_lst[0] == 0:
        floor = each_lst[0]
        room -= 1
    
    room_num = "0"+str(room)
    answer = str(floor) + room_num[-2:]

    print(answer)