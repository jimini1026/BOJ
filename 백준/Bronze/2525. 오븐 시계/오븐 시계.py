A,B=map(int,input().split())
C=int(input())
D=B+C

if A>24:
    A=A%24

print((A+(D//60))%24, D%60)