N=int(input())
list=list(map(int,input().split()))
if N==len(list):
    print(min(list),max(list))