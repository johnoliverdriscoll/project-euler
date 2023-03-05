from math import log10

def is_palindrome(n):
  d = int(log10(n))
  while d > 0:
    if n // (10 ** d) != n % 10:
      return False
    n = (n % (10 ** d)) // 10
    d -= 2
  return True

def reverse(n):
  m = 0
  while n:
    m *= 10
    m += n % 10
    n //= 10
  return m

def is_lychrel(n):
  c = 0
  while c < 50:
    n += reverse(n)
    if is_palindrome(n):
      return False
    c += 1
  return True

c = 0
for i in range(1, 10000):
  if is_lychrel(i):
    c += 1
print(c)
