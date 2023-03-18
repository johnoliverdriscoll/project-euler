from sys import argv

n = int(argv[1])
f = 1
for x in range(1, n + 1):
  f *= x
print(sum([int(c) for c in str(f)]))
