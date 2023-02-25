def factorize(n, f = None):
  if not f:
    f = set()
  f |= set([1, n])
  x = 2
  l = n // 2
  while x < l:
    if n % x == 0:
      l = n // x
      f.add(x)
      if not n // x in f:
        f |= factorize(n // x, f)
    x += 1
  return f

def proper_divisors(n):
  return factorize(n) - set([n])

a = set(filter(lambda n: sum(proper_divisors(n)) > n, range(2, 28123)))
n = set(range(1, 28123))
for x in a:
  n -= set([x + x])
  for y in a - set([x]):
    n -= set([x + y])
print(sum(n))
