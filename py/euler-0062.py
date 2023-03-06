import sys

def tuple_to_int(digits):
  return sum(map(
    lambda t: t[0] * 10 ** t[1],
    zip(digits, reversed(range(0, len(digits))))
  ))

def int_to_tuple(n):
  l = tuple()
  while n:
    l = l + (n % 10,)
    n //= 10
  return tuple(reversed(l))

def permutate(s, not_first=0):
  if len(s) == 1:
    yield s
  else:
    for i in range(0, len(s)):
      if not_first == None or s[i] != not_first:
        for t in permutate(s[:i] + s[i + 1:], None):
          yield (s[i],) + t

n = int(sys.argv[1])
x = 1
perfect_cubes = set()
while True:
  x3 = x ** 3
  perfect_cubes.add(x3)
  perfect_cube_permutations = []
  for p in set(permutate(int_to_tuple(x3))):
    y = tuple_to_int(p)
    if y in perfect_cubes:
      perfect_cube_permutations.append(y)
      if len(perfect_cube_permutations) == n:
        print(min(perfect_cube_permutations))
        exit()
  x += 1
