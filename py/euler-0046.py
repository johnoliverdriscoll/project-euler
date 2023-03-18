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

def is_goldbach_composite(n):
  if is_prime(n):
    return False
  for a in range(1, int((n // 2) ** (1 / 2)) + 1):
    if is_prime(n - 2 * a ** 2):
      return True
  return False

n = 9
while 1:
  if not is_prime(n) and not is_goldbach_composite(n):
    print(n)
    exit()
  n += 2
