import sys
n = int(sys.argv[1])
sum = 2
a = 1
b = 2
while a + b < n:
  c = a + b
  a, b = b, c
  if c % 2 == 0:
    sum += c
print(sum)
