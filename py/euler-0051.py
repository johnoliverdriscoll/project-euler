import sys

def is_prime(n, p = dict()):
  if n in p:
    return p[n]
  if n < 2:
    return False
  for x in range(2, int(n ** (1 / 2)) + 1):
    if n % x == 0:
      p[n] = False
      break
  if not n in p:
    p[n] = True
  return p[n]

def list_to_int(digits):
  return sum(map(
    lambda t: t[0] * 10 ** t[1],
    zip(digits, reversed(range(0, len(digits))))
  ))

def int_to_list(n):
  l = list()
  while n:
    l.append(n % 10)
    n //= 10
  l.reverse()
  return l

def get_digit_freq(n):
  freq = dict()
  while n:
    d = n % 10
    n //= 10
    freq[d] = freq.get(d, 0) + 1
  return freq

def get_rep_tuples(n):
  freq = get_digit_freq(n)
  rep_digits = set(freq.keys())
  l = int_to_list(n)
  return dict(
    list(
      filter(
        lambda pair: pair[1] != tuple([None] * len(l)),
        map(
          lambda rep_digit: (rep_digit, tuple(list(map(lambda d: None if d == rep_digit else d, l)))),
          rep_digits
        )
      )
    )
  )

n = int(sys.argv[1])
visited = set()
i = 1
while True:
  reps = get_rep_tuples(i)
  if len(reps) and is_prime(i):
    for d in reps:
      if not reps[d] in visited:
        visited.add(reps[d])
        replacement = 0
        not_prime = 0
        prime = 1
        while replacement < 10 and 10 - not_prime >= n:
          if replacement == d or (replacement == 0 and reps[d][0] == None):
            replacement += 1
            continue
          v = list_to_int(list(map(lambda d: replacement if d == None else d, reps[d])))
          if is_prime(v):
            prime += 1
          else:
            not_prime += 1
          replacement += 1
        if prime == n:
          print(i)
          exit()
  i += 1
