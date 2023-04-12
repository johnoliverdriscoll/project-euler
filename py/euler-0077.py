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

def get_primes_less_than(n, memo=dict()):
  primes = memo.get(n, None)
  if primes == None:
    prime = get_prime()
    primes = []
    while (p := next(prime)) < n:
      primes.append(p)
    memo[n] = primes
  return primes

def permutate_sum(n, m=None, memo=dict()):
  if m == None:
    m = n
  if n == 2 or n == 0:
    return 1
  count = memo.get((n, m), None)
  if count == None:
    count = 0
    for i in get_primes_less_than(m):
      count += permutate_sum(n - i, min(n - i + 1, i + 1))
    memo[(n, m)] = count
  return count

n = 1
while 1:
  if permutate_sum(n) > 5000:
    print(n)
    exit()
  n += 1
