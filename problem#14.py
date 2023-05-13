def make_collatz(num):
  lst = []
  while num > 1:
    if num % 2 == 0:
      num = num / 2
    else:
      num = 3 * num + 1
    lst.append(num)
  return lst


def count_chain(num):
  if num == 1:
    return 1
  if num % 2 == 0:
    return 1 + count_chain(num / 2)
  else:
    return 1 + count_chain(3 * num + 1)


maxm = -1e7
ans = 1
for num in range(1, 1000000):
  print(f'current ans is {ans} and number is {num}.')
  num_lst = make_collatz(num)
  if maxm < len(num_lst):
    ans = num
    maxm = len(num_lst)
