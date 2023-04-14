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

def amicable_chain(n, l, memo=dict()):
  c = memo.get(n, None)
  if c == None:
    c = [n]
    s = set(c)
    while 1:
      n = sum(proper_divisors(n))
      if n < l and n == c[0]:
        break
      elif n > l or n in s:
        c = None
        break
      c.append(n)
      s.add(n)
    if c:
      c = tuple(c)
      for i in range(0, len(c)):
        memo[c[i]] = c[i:] + c[:i]
  return c

m = None
for n in range(1, 15000):
  c = amicable_chain(n, 1000000)
  if c and (m == None or len(m) < len(c)):
    m = c
print(min(m))
