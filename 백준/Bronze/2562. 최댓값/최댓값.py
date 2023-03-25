list=[]
for i in range(9):
    list.append(int(input()))
print(max(list),list.index(max(list))+1,sep="\n")