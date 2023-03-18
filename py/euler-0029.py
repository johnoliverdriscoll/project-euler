from sys import argv

n = int(argv[1])
t = set()
for a in range(2, n + 1):
  for b in range(2, n + 1):
    t.add(a ** b)
print(len(t))
