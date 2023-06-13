import string

string_dict = (dict(zip(string.ascii_lowercase, range(1, 27))))

file1 = open("names.txt", "r")
lines = (file1.readlines())
sorted_lines = (sorted([i for i in lines[0].split(',')]))

res = 0
for i, name in enumerate(sorted_lines):
  rank1 = sum([string_dict.get(ch.lower(), 0) for ch in name])
  print(rank1)
  res += (i + 1) * rank1

print(res)
