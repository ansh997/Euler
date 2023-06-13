from math import factorial

n = 100
ans = factorial(n)
print(sum([int(i) for i in str(ans)]))
