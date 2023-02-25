import sys

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

s = 0
f = set()
for a in range(2, 10000):
  if a in f:
    continue
  b = sum(proper_divisors(a))
  if a != b and sum(proper_divisors(b)) == a:
    s += a + b
    f.add(b)
print(s)
