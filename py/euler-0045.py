def is_pentagonal(n):
  return (1 + (1 + 24 * n) ** (1 / 2)) % 6 == 0

def is_triangular(n):
  return ((1 + 8 * n) ** (1 / 2) - 1) % 2 == 0

def is_hexagonal(n):
  return (1 + (1 + 8 * n) ** (1 / 2)) % 4 == 0

def triangular(n):
  return (n * (n + 1)) // 2

n = 286
while 1:
  t = triangular(n)
  if is_pentagonal(t) and is_hexagonal(t):
    print(t)
    exit()
  n += 1
