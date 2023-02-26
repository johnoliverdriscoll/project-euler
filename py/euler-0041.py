def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

def next_pandigital(n):
  d = str(n)
  i = len(d) - 1
  while i > 0 and int(d[i - 1]) < int(d[i]):
    i -= 1
  if i == 0:
    return int(d[::-1][1:])
  n = next(filter(lambda n: int(n) < int(d[i - 1]), reversed(sorted(d[i:]))))
  return int(d[:i - 1] + n + ''.join(list(filter(lambda m: m != n, reversed(sorted(d[i - 1:i] + d[i:]))))))

d = 987654321
while not is_prime(d):
  d = next_pandigital(d)
print(d)
