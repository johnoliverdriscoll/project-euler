import sys
e = int(sys.argv[1])
m = 10 ** (e - 1)
n = 10 ** e - 1
x = n
q = n * n
while x >= m:
  y = n
  while y >= x:
    p = x * y
    if p > q:
      break
    c = list(str(p))
    is_palindrome = True
    while len(c) > 1:
      if not c.pop(0) == c.pop():
        is_palindrome = False
        break
    if is_palindrome:
      print(p)
      exit()
    y -= 1
  x -= 1
  q = p
