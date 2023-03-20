from sys import argv

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
  f.add(1)
  f.add(n)
  x = 2
  l = n // 2
  while x <= l:
    if n % x == 0:
      l = n // x
      f.add(x)
      if not n // x in f:
        for y in factorize(n // x, f):
          f.add(y)
    x += 1
  return f

def count_distinct_prime_factors(x, n, f = dict()):
  for i in range(x, x + n):
    if not i in f:
      f[i] = factorize(i)
    if len([x for x in f[i] - set([1, i]) if is_prime(x)]) != n:
      return i - x
  return n

n = int(argv[1])
x = 0
while 1:
  c = count_distinct_prime_factors(x, n)
  if c == n:
    print(x)
    exit()
  x += c + 1
