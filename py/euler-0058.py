def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      return False
  return True

p = 0
t = 1
i = 1
l = 1
while p == 0 or p / t >= .10:
  for _ in range(0, 4):
    i += l + 1
    if is_prime(i):
      p += 1
    t += 1
  l += 2
print(l)
