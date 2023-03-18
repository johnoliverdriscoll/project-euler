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

def is_circular_prime(n):
  if not is_prime(n):
    return False
  s = str(n)
  for _ in range(1, len(s)):
    s = s[1:] + s[0]
    if not is_prime(int(s)):
      return False
  return True

n = int(argv[1])
print(len([n for n in range(2, n) if is_circular_prime(n)]))
  
