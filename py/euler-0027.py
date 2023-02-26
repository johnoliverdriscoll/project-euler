def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

m = 0
p = None
for a in range(-1000, 1001):
  for b in range(-1000, 1001):
    n = 0
    while True:
      x = int(n ** 2 + a * n + b)
      if not is_prime(x):
        break
      n += 1
    if n > m:
      m = n
      p = a * b
print(p)
