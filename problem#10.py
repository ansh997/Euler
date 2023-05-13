import math

till = 2000000
print(math.sqrt(till))
ans = 0
primes = [True for i in range(till + 1)]
p = 2
while p * p <= till:
  if primes[p]:
    for i in range(p * p, till + 1, p):
      primes[i] = False
  p += 1

for p in range(2, till + 1):
  if primes[p]:
    ans += p
print(ans)
