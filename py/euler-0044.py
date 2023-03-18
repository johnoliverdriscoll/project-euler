def is_pentagonal(n):
  return (1 + (1 + 24 * n) ** (1 / 2)) % 6 == 0

def pentagonal(n):
  return (n * (3 * n - 1)) // 2

i = 1
while 1:
  for j in reversed(range(1, i + 1)):
    if is_pentagonal(pentagonal(i) + pentagonal(j)) \
       and is_pentagonal(pentagonal(i) - pentagonal(j)):
      print(pentagonal(i) - pentagonal(j))
      exit()
  i += 1
