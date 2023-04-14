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

def proper_divisors(n):
  return factorize(n) - set([n])

a = set([n for n in range(2, 28123) if sum(proper_divisors(n)) > n])
n = set(range(1, 28123))
for x in a:
  n -= set([x + x])
  for y in a - set([x]):
    n -= set([x + y])
print(sum(n))
