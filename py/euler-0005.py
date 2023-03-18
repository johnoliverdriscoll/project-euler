from sys import argv

n = int(argv[1])
p = 1
for x in range (2, n + 1):
  if p % x:
    p *= x
    for y in range(2, x):
      if x % y == 0:
        p //= x // y
        break
# You could also just use lcm for this, but where's the fun in that?
print(p)
