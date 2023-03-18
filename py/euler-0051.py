from sys import argv

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

def list_to_int(d):
  return sum([t[0] * 10 ** t[1] for t in zip(d, reversed(range(0, len(d))))])

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
  l = int_to_list(n)
  return dict(
    [pair for pair in [
      (rep, tuple([
        None if d == rep else d for d in l
      ])) for rep in set(get_digit_freq(n).keys())
    ] if pair[1] != tuple([None] * len(l))]
  )

n = int(argv[1])
visited = set()
i = 1
while 1:
  reps = get_rep_tuples(i)
  if len(reps) and is_prime(i):
    for d in reps:
      if not reps[d] in visited:
        visited.add(reps[d])
        replacement = 0
        not_prime = 0
        prime = 1
        while replacement < 10 and 10 - not_prime >= n:
          if replacement != d and (replacement != 0 or reps[d][0] != None):
            v = list_to_int([replacement if d == None else d for d in reps[d]])
            if is_prime(v):
              prime += 1
            else:
              not_prime += 1
          replacement += 1
        if prime == n:
          print(i)
          exit()
  i += 1
