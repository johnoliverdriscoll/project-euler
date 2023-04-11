from os import path

RULE_1 = """
Numerals must be arranged in descending order of size.
"""

RULE_2 = """
M, C, and X cannot be equalled or exceed by smaller denominations.
"""

RULE_3 = """
D, L, and V can each only appear once.
"""

RULE_I = """
Only one I, X, and C can be used as the leading numeral in part of a subtractive
pair.
"""

RULE_II = """
I can only be placed before V and X.
"""

RULE_III = """
X can only be placed before L and C.
"""

RULE_IV = """
C can only be placed before D and M.
"""

numeral_values = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

subtractive_pairs = {
  'IV': 4,
  'IX': 9,
  'XL': 40,
  'XC': 90,
  'CD': 400,
  'DM': 900,
}

def subtractive_pair_to_int(p, n, c):
  if p == None:
    return numeral_values[n] * c
  return numeral_values[n] - numeral_values[p]

def roman_numeral_to_int(r):
  # Parse numerals into groups.
  i = 0
  groups = []
  freq = dict()
  while i < len(r):
    n = r[i]
    c = 1
    i += 1
    while i < len(r) and r[i] == n:
      c += 1
      i += 1
    freq[n] = freq.get(n, 0) + c
    groups.append((n, c))
  # Identify subtractive pairs.
  i = 0
  pairs = []
  while i < len(groups):
    n, c = groups[i]
    is_subtractive_pair = False
    if i + 1 < len(groups):
      m, d = groups[i + 1]
      if numeral_values[n] < numeral_values[m]:
        # Enforce rule i.
        if not n in ['I', 'X', 'C'] or c > 1:
          raise RuntimeError(RULE_I)
        # Enforce rule ii.
        if n == 'I' and m not in ['V', 'X']:
          raise RuntimeError(RULE_II)
        # Enfore rule iv.
        if n == 'X' and m not in ['L', 'C']:
          raise RuntimeError(RULE_III)
        if n == 'C' and m not in ['D', 'M']:
          raise RuntimeError(RULE_IV)
        is_subtractive_pair = True
        pairs.append((n, m, 1))
        if d > 1:
          pairs.append((None, m, d - 1))
        i += 1
    if not is_subtractive_pair:
      pairs.append((None, n, c))
    i += 1
  # Enforce rule 1.
  i = 0
  values = [subtractive_pair_to_int(*pair) for pair in pairs]
  while i < len(values) - 1:
    if values[i] <= values[i + 1]:
      raise RuntimeError(RULE_1)
    i += 1
  # Enforce rule 2.
  for p, n, c in pairs:
    for x in ['M', 'C', 'X']:
      if numeral_values[x] > numeral_values[n] \
         and numeral_values[n] * c >= numeral_values[x]:
        print(r)
        raise RuntimeError(RULE_2)
  # Enforce rule 3.
  for x in ['D', 'L', 'V']:
    if freq.get(x, 0) > 1:
      raise RuntimeError(RULE_3)
  return sum(values)

def roman_numeral_from_int(v):
  r = ''
  for x, n in list(reversed(sorted([
    (x, n) for n, x in
    list(numeral_values.items()) + list(subtractive_pairs.items())
  ]))):
    r += n * (v // x)
    v -= x * (v // x)
  return r

f = open(path.join(path.dirname(__file__), '../resources/p089_roman.txt'))
n = [l.strip() for l in f]
print(
  sum([len(x) for x in n])
  - sum([len(roman_numeral_from_int(roman_numeral_to_int(x))) for x in n])
)
