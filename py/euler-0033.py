def factorize(n, memo=dict()):
  if n < 2:
    return set()
  f = memo.get(n, None)
  if f == None:
    f = set()
    f.add(1)
    f.add(n)
    x = 2
    l = n // 2
    sqrt_n = int(n ** (1 / 2)) + 1
    while x <= l:
      if x > sqrt_n and len(f) == 2:
        return f
      if n % x == 0:
        l = n // x
        f.add(x)
        if not n // x in f:
          for y in factorize(n // x):
            f.add(y)
      x += 1
    memo[n] = f
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
