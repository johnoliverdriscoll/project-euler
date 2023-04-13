from math import gcd
from sys import argv

n = int(argv[1])
count = 0
for x1 in range(0, n + 1):
  for y1 in range(0, n + 1):
    for x2 in range(0, x1 + 1):
      for y2 in range(y1, n + 1):
        if not (x1 == 0 and y1 == 0):
          if not x1 == x2 or not y1 == y2:
            if x2 == 0 and y2 == 0:
              if x1 > 0 and y1 > 0:
                count += 1
            else:
              dy = y2 - y1
              dx = x2 - x1
              if dx == 0 and y1 == 0:
                count += 1
              else:
                ga = gcd(dx, dy)
                gb = gcd(x1, y1)
                gc = gcd(x2, y2)
                if (y1 // gb == x2 // gc and x1 // gb == -y2 // gc) \
                   or (y1 // gb == -x2 // gc and x1 // gb == y2 // gc) \
                   or (dy // ga == x1 // gb and dx // ga == -y1 // gb) \
                   or (dy // ga == -x1 // gb and dx // ga == y1 // gb) \
                   or (dy // ga == x2 // gc and dx // ga == -y2 // gc) \
                   or (dy // ga == -x2 // gc and dx // ga == y2 // gc):
                  count += 1
print(count)
