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

x = 1
for p in get_prime():
  if x * p > int(argv[1]):
    print(x)
    exit()
  else:
    x *= p
