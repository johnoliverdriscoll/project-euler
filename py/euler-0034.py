from math import factorial

x = 3
s = 0
while x < factorial(9):
  if x == sum([factorial(int(n)) for n in str(x)]):
    s += x
  x += 1
print(s)
