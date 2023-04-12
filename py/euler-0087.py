from sys import argv

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

def get_prime():
  yield 2
  p = 3
  while 1:
    if is_prime(p):
      yield p
    p += 2

n = int(argv[1])
prime_power_triples = set()
i = get_prime()
while 1:
  x = next(i)
  s = x ** 2
  if s >= n:
    break
  j = get_prime()
  while 1:
    y = next(j)
    s += y ** 3
    if s >= n:
      s -= y ** 3
      break
    k = get_prime()
    while 1:
      z = next(k)
      s += z ** 4
      if s >= n:
        s -= z ** 4
        break
      prime_power_triples.add(s)
      s -= z ** 4
    s -= y ** 3

print(len(prime_power_triples))
