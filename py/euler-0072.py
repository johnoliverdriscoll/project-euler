from sys import argv
from sympy.ntheory.factor_ import totient

n = int(argv[1])
count = 0
for i in range(2, n + 1):
  count += totient(i)
print(count)
