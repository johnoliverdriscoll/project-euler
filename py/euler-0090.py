from itertools import combinations

pairs = [
  ((0,), (1,)),
  ((0,), (4,)),
  ((0,), (6, 9)),
  ((1,), (6, 9)),
  ((2,), (5,)),
  ((3,), (6, 9)),
  ((4,), (6, 9)),
  ((6, 9), (4,)),
  ((8,), (1,)),
]

def can_display_pairs(d1, d2, pairs):
  for p1, p2 in pairs:
    if not (set(d1) & set(p1) and set(d2) & set(p2)) \
       and not (set(d1) & set(p2) and set(d2) & set(p1)):
      return False
  return True

def generate_dice(pairs):
  d = set(range(0, 10))
  for d1 in combinations(d, 6):
    for d2 in combinations(d, 6):
      yield (d1, d2)

n = [1 for d1, d2 in generate_dice(pairs) if can_display_pairs(d1, d2, pairs)]
print(sum(n) // 2)
