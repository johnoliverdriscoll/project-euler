from math import log10
from itertools import combinations
from sys import argv

def is_prime(n, p = dict()):
  if n in p:
    return p[n]
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      p[n] = False
      break
  if not n in p:
    p[n] = True
  return p[n]

def iter_prime():
  yield 2
  n = 3
  while True:
    if is_prime(n):
      yield n
    n += 2

def is_prime_concatenation(p, q):
  return is_prime(p * 10 ** int(1 + log10(q)) + q) \
    and is_prime(q * 10 ** int(1 + log10(p)) + p)

def is_prime_combination(C, Q):
  for (p, q) in combinations(C, 2):
    if p not in Q[q]:
      return False
  return True

k = int(argv[1])
Q = dict()
prime = iter_prime()
while 1:
  p = next(prime)
  Qp = list()
  for q in Q:
    if is_prime_concatenation(p, q):
      Qp.append(q)
  for C in combinations(Qp, k - 1):
    if is_prime_combination(C, Q):
      print(p + sum(C))
      exit()
  Q[p] = Qp
