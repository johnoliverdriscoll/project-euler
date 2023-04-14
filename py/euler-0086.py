from sys import argv

def pythagorean_triple(k, m, n):
  return k * 2 * m * n, k * (m ** 2 - n ** 2), k * (m ** 2 + n ** 2)

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

def is_perfect_square(x):
  x = abs(x)
  return round(x ** (1 / 2)) ** 2 == x

# Calculate a list of all pythagorean triples a ** 2 + b ** 2 = c ** 2 where
# a or b equal M.
def associated_pythagorean_triples(M):
  triples = set()
  for k in proper_divisors(M):
    M_k = M // k
    # M might be k * 2 * m * n.
    if M_k % 2 == 0:
      M_k_2 = M_k // 2
      for n in proper_divisors(M_k_2):
        m = M_k_2 // n
        if n < m and  k * (m ** 2 - n ** 2) <= M * 2:
          triples.add(pythagorean_triple(k, m, n))
    # M might be k * (m ** 2 - n ** 2).
    # Is there some trick to determine if some number is the delta between two
    # squares? That would save some time here instead of brute forcing it.
    for m in range(int(M_k ** (1 / 2)) + 1,  M):
      n2 = m ** 2 - M_k
      if is_perfect_square(n2):
        n = int(n2 ** (1 / 2))
        if k * 2 * m * n <= M * 2:
          triples.add(pythagorean_triple(k, m, n))
  return triples

def is_int_shortest_route(a, b, c):
  return is_perfect_square(min([
    a ** 2 + (b + c) ** 2,
    b ** 2 + (a + c) ** 2,
    c ** 2 + (a + b) ** 2,
  ]))
  
n = int(argv[1])

M = 1
count = 0
while count <= n:
  M += 1
  # The inner loop produces duplicates within itself, so a set must be used
  # here to dedup cuboids. The inner loop does not produce collisions with
  # previous values of M, however, that doesn't seem to make much difference
  # in terms of total runtime for a given n.
  cuboids = set()
  for t in associated_pythagorean_triples(M):
    x, y = sorted((t[0], t[1]))
    a, bc = x, y
    if a <= M:
      l, u = max(1, bc - M), min(bc, M)
      for b in range(l, (l + u) // 2 + 1):
        c = bc - b
        if a == M or b == M or c == M and is_int_shortest_route(a, b, c):
          cuboids.add(tuple(sorted((a, b, c))))
    ab, c = x, y
    if c <= M:
      l, u = max(1, ab - M), min(ab, M)
      for a in range(l, (l + u) // 2 + 1):
        b = ab - a
        if a == M or b == M or c == M and is_int_shortest_route(a, b, c):
          cuboids.add(tuple(sorted((a, b, c))))
  count += len(cuboids)
print(M)
