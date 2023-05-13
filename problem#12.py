# Below code from: https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
from math import sqrt
from functools import reduce

##############################################################
### cartesian product of lists ##################################
##############################################################


def appendEs2Sequences(sequences, es):
  result = []
  if not sequences:
    for e in es:
      result.append([e])
  else:
    for e in es:
      result += [seq + [e] for seq in sequences]
  return result


def cartesianproduct(lists):
  """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
  return reduce(appendEs2Sequences, lists, [])


##############################################################
### prime factors of a natural ##################################
##############################################################


def primefactors(n):
  '''lists prime factors, from greatest to smallest'''
  i = 2
  while i <= sqrt(n):
    if n % i == 0:
      l = primefactors(n / i)
      l.append(i)
      return l
    i += 1
  return [n]  # n is prime


##############################################################
### factorization of a natural ##################################
##############################################################


def factorGenerator(n):
  p = primefactors(n)
  factors = {}
  for p1 in p:
    try:
      factors[p1] += 1
    except KeyError:
      factors[p1] = 1
  return factors


def divisors(n):
  factors = factorGenerator(n)
  divisors = []
  listexponents = [
    map(lambda x: k**x, range(0, factors[k] + 1)) for k in factors.keys()
  ]
  listfactors = cartesianproduct(listexponents)
  for f in listfactors:
    divisors.append(reduce(lambda x, y: x * y, f, 1))
  divisors.sort()
  return divisors


def get_triangle_number(num):
  res = 0
  while num != 0:
    res += num
    num -= 1
  return res


def add_num_upto(n):
  return int((n * (n + 1)) / 2)


def get_divisors(number):
  ans = []
  for i in range(1, number + 1):
    if number % i == 0:
      ans.append(i)
  return ans


# number = int(100000)
# tr_num = (add_num_upto(number))
# print(tr_num)
# num_of_divisors = len(divisors(tr_num))
# print(num_of_divisors)
start = 1
while True:
  tr_num = add_num_upto(start)
  num_of_divisors = len(divisors(tr_num))
  print(f'Start = {start}, Triangular Number: {tr_num}, {num_of_divisors}.')
  if num_of_divisors >= 500:
    print(f'Answer is {start} and number of divisors are {num_of_divisors}')
    break
  start += 1
