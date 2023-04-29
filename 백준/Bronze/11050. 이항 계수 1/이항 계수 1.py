N, K = map(int, input().split())

import math as m
value = int(m.factorial(N)/(m.factorial(N-K) * m.factorial(K)))
print(value)