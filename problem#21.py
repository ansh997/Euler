import time
import math
from functools import lru_cache


@lru_cache(None)
def sum_div(n):
  # Taken from AJNeufeld's answer
  total = 1
  for x in range(2, int(math.sqrt(n) + 1)):
    if n % x == 0:
      total += x
      y = n // x
      if y > x:
        total += y
  return total


def amicable_numbers(limit):
  for a in range(limit):
    b = sum_div(a)
    if a != b and sum_div(b) == a:
      yield a


n = 10000


def get_divisors(n):
  for i in range(1, int(n / 2) + 1):
    if n % i == 0:
      yield i
  # yield n


def d(n):
  res_list = get_divisors(n)
  return sum(res_list)


def solve(end=n):
  res = 0
  done = []
  for a in range(n + 1):
    # print(a, end=' ')
    if a in done:
      # print(a, 'already done.')
      continue
    b = d(a)
    if d(b) == a and a != b:
      # print('amicable', a, b)
      res += a + b
      done.append(a)
      done.append(b)
    # print('')
  return res


t0 = time.time()
# print(solve(n))
print(sum(amicable_numbers(10000)))
print(time.time() - t0)
