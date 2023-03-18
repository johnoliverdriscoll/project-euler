from sys import argv

n = int(argv[1])
sum = 0
for x in range(3, n, 3):
  sum += x
for x in range(5, n, 5):
  if x % 3:
    sum += x
print(sum)
