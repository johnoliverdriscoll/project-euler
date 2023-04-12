def check_primality_for_n_gt_2(n):
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

def is_prime(n, memo=dict()):
  if n < 2:
    return False
  if n == 2:
    return True
  p = memo.get(n, None)
  if p == None:
    p = check_primality_for_n_gt_2(n)
    memo[n] = p
  return p

def gen_primes():
  yield 2
  p = 3
  while 1:
    if is_prime(p):
      yield p
    p += 2

primes = []
ratio, n = None, None
prime = gen_primes()
while (p := next(prime)) < 10 ** (7 // 2 + 1):
  for q in reversed(primes):
    r = p * q
    if r >= 10 ** 7:
      continue
    t = (p - 1) * (q - 1)
    if sorted(list(str(r))) == sorted(list(str(t))):
      if ratio == None or ratio > r / t:
        ratio, n = r / t, r
  primes.append(p)
print(n)
