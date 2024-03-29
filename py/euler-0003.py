from sys import argv

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

n = int(argv[1])
for x in range(2, n):
  if n % x == 0:
    d = n // x
    if is_prime(d):
      print(d)
      exit()
