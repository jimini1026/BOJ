num=int(input())
list=[]
for i in range(num):
    a,b=map(int,input().split())
    list.append(a+b)
for g in list:
    print(g)