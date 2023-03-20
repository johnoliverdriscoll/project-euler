from sys import argv

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

n = int(argv[1])
z = 1
t = 0
while 1:
  t += z
  z += 1
  if len(factorize(t)) > n:
    print(t)
    exit()
