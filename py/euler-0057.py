from math import log10

def sqrt2():
  n = 3
  d = 2
  yield (n, d)
  while 1:
    n, d = n + 2 * d, n + d
    yield (n, d)

it = sqrt2()
c = 0
for i in range(0, 1000):
  n, d = next(it)
  if int(log10(n)) > int(log10(d)):
    c += 1
print(c)
