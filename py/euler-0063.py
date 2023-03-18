c = 0
e = 1
while 1:
  b = 1
  d = c
  while 1:
    l = len(str(b ** e))
    if l == e:
      c += 1
    elif l > e:
      break
    b += 1
  if d == c:
    break
  e += 1
print(c)
