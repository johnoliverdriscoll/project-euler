import sys

n = int(sys.argv[1])
i = 1
while True:
  if len(str(i)) != len(set(str(i))):
    i += 1
    continue
  found = True
  for j in range(2, n + 1):
    if set(str(i * j)) != set(str(i)):
      found = False
      break
  if found:
    print(i)
    exit()
  i += 1
