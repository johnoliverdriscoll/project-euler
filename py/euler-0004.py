from sys import argv

def is_palindrome(l):
  c = l.copy()
  while len(c) > 1:
    if not c.pop(0) == c.pop():
      return False
  return True

e = int(argv[1])
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
    if is_palindrome(list(str(p))):
      print(p)
      exit()
    y -= 1
  x -= 1
  q = p
