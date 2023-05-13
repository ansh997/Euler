#time module to calculate the time
import time

#time at the start of execution
start_time = time.time()


#function to find the pythagorean triplet
#Using Dickson formula
def pythagorean_triplet_dickson():
  for r in range(1, 1000):
    for s in range(1, r):
      if ((r**2) / 2) % s == 0:
        t = int((r**2 / 2) / s)  # Why??
        print(r, s, t)
        if (r + s) + (r + t) + (r + t + s) == 1000:
          print(((r + s), (r + t), (r + t + s)))
          return (r + s) * (r + t) * (r + t + s)


#Printing the result
print(pythagorean_triplet_dickson())

#time at the end of execution
end_time = time.time()

#Total time taken for execution
print(end_time - start_time)

# Second Approach
# for c in range(413, 500):
#   c2 = c**2
#   for a in range(max(1, 1000 - c - (c - 1)), min(332, (1000 - c) // 2) + 1):
#     b = 1000 - c - a
#     if a**2 + b**2 == c2:
#       print(a, b, c, a * b * c)
