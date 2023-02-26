def permutate(s, not_first='0'):
  if not len(s):
    yield ''
  else:
    for i in range(0, len(s)):
      if not not_first or s[i] != not_first:
        for t in permutate(s[:i] + s[i + 1:], None):
          yield s[i] + t

s = 0
for p in permutate('1234567890'):
  if int(p[1:4]) % 2 == 0 \
     and int(p[2:5]) % 3 == 0 \
     and int(p[3:6]) % 5 == 0 \
     and int(p[4:7]) % 7 == 0 \
     and int(p[5:8]) % 11 == 0 \
     and int(p[6:9]) % 13 == 0 \
     and int(p[7:]) % 17 == 0:
    s += int(p)
print(s)
