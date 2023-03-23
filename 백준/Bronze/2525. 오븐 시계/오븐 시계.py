A,B=map(int,input().split())
C=int(input())
D=B+C

if A>24:
    A=A%24

if D<60:
    print(A,D)
else:
    if A+(D//60)<24:
        print(A+(D//60),D%60)
    else: #D>=60 and A+(D//60)>=24
        print((A+(D//60))%24,D%60)