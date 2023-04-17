b = 28433 * (1 << 7830457) + 1
s = []
while len(s) < 10:
  s.append(b % 10)
  b //= 10
print(''.join([str(d) for d in reversed(s)]))
