def factorize(n, f = None):
  if not f:
    f = set()
  f.add(1)
  f.add(n)
  x = 2
  l = n // 2
  while x < l:
    if n % x == 0:
      l = n // x
      f.add(x)
      if not n // x in f:
        for y in factorize(n // x, f):
          f.add(y)
    x += 1
  return f

def proper_divisors(n):
  return factorize(n) - set([n])

a = set([n for n in range(2, 28123) if sum(proper_divisors(n)) > n])
n = set(range(1, 28123))
for x in a:
  n -= set([x + x])
  for y in a - set([x]):
    n -= set([x + y])
print(sum(n))
