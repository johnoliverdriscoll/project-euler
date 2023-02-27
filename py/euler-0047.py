import sys

def is_prime(n, p = dict()):
  if n in p:
    return p[n]
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      p[n] = False
      break
  if not n in p:
    p[n] = True
  return p[n]

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

def count_distinct_prime_factors(x, n, f = dict()):
  for i in range(x, x + n):
    if not i in f:
      f[i] = factorize(i)
    if len(list((filter(is_prime, f[i] - set([1, i]))))) != n:
      return i - x
  return n

n = int(sys.argv[1])
x = 0
while True:
  c = count_distinct_prime_factors(x, n)
  if c == n:
    print(x)
    exit()
  x += c + 1
