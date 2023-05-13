print(str((2)**1000))
digits = str((2)**1000)
ans = 0
for elem in digits:
  ans += int(elem)
print(ans)