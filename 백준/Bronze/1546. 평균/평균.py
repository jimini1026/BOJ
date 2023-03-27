n = int(input())
list = list(map(int,input().split()))
M = max(list)

average=0
for i in range(len(list)):
    average += (list[i]/M)*100
print(average / n)