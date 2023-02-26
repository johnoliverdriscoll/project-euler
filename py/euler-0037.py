n = 1
l = 0
while n < 100000:
  s = ''
  m = 1
  while len(s) < 9:
    s += str(n * m)
    m += 1
  if len(s) == 9 and set(s) == set('123456789'):
    if l < int(s):
      l = int(s)
  n += 1
print(l)
