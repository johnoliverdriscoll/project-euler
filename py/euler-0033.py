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

n = 1
d = 1
for i in range(11, 100):
  for j in range(i + 1, 100):
    if i % 10 == 0 or j % 10 == 0:
      continue
    if (i % 10 == j // 10 and i / j == (i // 10) / (j % 10)) \
       or (i // 10 == j % 10 and i / j == (i % 10) / (j // 10)):
      n *= i
      d *= j
fd = factorize(d)
for f in reversed(sorted(list(factorize(n)))):
  if f in fd:
    print(d // f)
    exit()
