from math import log
from os import path

f = open(path.join(path.dirname(__file__), '../resources/p099_base_exp.txt'))
be = [[int(n) for n in l.strip().split(',')] for l in f]
m, j = 0, 0
for i in range(0, len(be)):
  b, e = be[i]
  p = log(b) * e
  if m < p:
    m, j = p, i
print(j + 1)
