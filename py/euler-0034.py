def factorial(n):
  if n == 0:
    return 1
  f = n
  for x in range(2, n):
    f *= x
  return f

x = 3
s = 0
while x < factorial(9):
  if x == sum([factorial(int(n)) for n in str(x)]):
    s += x
  x += 1
print(s)
