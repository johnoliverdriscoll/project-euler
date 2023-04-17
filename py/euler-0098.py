from os import path

f = open(path.join(path.dirname(__file__), '../resources/p098_words.txt'))
words = [w[1:-1] for w in f.readline().strip().split(',')]

def freq(s):
  f = dict()
  for c in s:
    f[c] = f.get(c, 0) + 1
  return f

def canonical_key(s, word=None, symbols=None):
  if word and symbols:
    symbols = dict([(word[i], symbols[i]) for i in range(0, len(word))])
    curr = max(symbols.values()) + 1
  else:
    symbols = dict()
    curr = 0
  key = []
  for c in s:
    v = symbols.get(c, curr)
    if v == curr:
      curr += 1
      symbols[c] = v
    key.append(v)
  return tuple(key)

def get_anagrams(words):
  anagrams = dict()
  for i in range(0, len(words)):
    w = words[i]
    wf = sorted(freq(w).items())
    for j in range(i + 1, len(words)):
      o = words[j]
      if not w == o and len(w) == len(o):
        of = freq(o)
        k = tuple(zip(wf, sorted(of.items())))
        if all([a == b for a, b, in k]):
          ary = anagrams.get(k, [w])
          ary.append(o)
          anagrams[k] = ary
  return anagrams

def index(s):
  pairs = [
    (key, [(canonical_key(v, s[k][0], key), v) for v in s[k]])
    for k, key in [(k, canonical_key(s[k][0])) for k in s]
  ]
  keys = dict()
  for k, v in pairs:
    ary = keys.get(k, [])
    ary.append(v)
    keys[k] = ary
  return keys

def canonical_anagram(s, k, a):
  k = dict(zip(k, s))
  return ''.join([k[c] for c in a])

def is_perfect_square(x):
  x = abs(x)
  return round(x ** (1 / 2)) ** 2 == x


anagrams = get_anagrams(words)
anagrams_index = index(anagrams)

l = max([len(anagrams[k][0]) for k in anagrams])
n = 1
sq = list()
m = 0
while len(s := str(n ** 2)) <= l:
  k = canonical_key(s)
  if (A := anagrams_index.get(k, None)):
    for pairs in A:
      for pair in pairs[1:]:
        if is_perfect_square(a := int(canonical_anagram(s, k, pair[0]))):
          if len(str(a)) == len(s):
            if m < max(a, int(s)):
              m = max(a, int(s))
  n += 1
print(m)
