import sys

def is_prime(n, p = set()):
  if n in p:
    return True
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  p.add(n)
  return True

def is_circular_prime(n):
  if not is_prime(n):
    return False
  s = str(n)
  for _ in range(1, len(s)):
    s = s[1:] + s[0]
    if not is_prime(int(s)):
      return False
  return True

print(sum(map(is_circular_prime, range(2, int(sys.argv[1])))))
  
