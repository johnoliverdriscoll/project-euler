import sys

def factorization(n, f = None):
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
        f |= factorization(n // x, f)
    x += 1
  return f

n = int(sys.argv[1])
z = 1
t = 0
while True:
  t += z
  z += 1
  if len(factorization(t)) > n:
    print(t)
    exit()
