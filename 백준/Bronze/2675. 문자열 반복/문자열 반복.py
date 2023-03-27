list=[]
for _ in range(int(input())):
    num,text=input().split()
    for i in text:
        list.append(int(num)*i)
    print(*list,sep="")
    list.clear()