a,b,c,d,e=map(int,input().split())
f=[a,b,c,d,e]
g=0
for i in f:
    g+=i**2
print(g%10)