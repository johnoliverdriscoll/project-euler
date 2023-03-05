def factorial(n):
  if n == 0:
    return 1
  p = 1
  for x in range(2, n + 1):
    p *= x
  return p

c = 0
for n in range(0, 101):
  for r in range(1, n):
    if factorial(n) // (factorial(r) * factorial(n - r)) > 1000000:
      c += 1
print(c)
