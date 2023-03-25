list=[]
for i in range(9):
    list.append(int(input()))
max=0
for g in range(9):
    if max<list[g]:
        max=list[g]
print(max,list.index(max)+1,sep="\n")