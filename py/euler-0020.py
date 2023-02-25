import sys
n = int(sys.argv[1])
f = 1
for x in range(1, n + 1):
  f *= x
print(sum(map(lambda c: int(c), str(f))))
