A, B, V = map(int,input().split())
import math
day = math.ceil((-V + A)/(B - A) +1)

print(day)