from os import path

def is_triange_number(n, t = list()):
  while len(t) == 0 or t[len(t) - 1] < n:
    t.append(((len(t) + 1) * (len(t) + 2)) // 2)
  return n in t

def is_triangle_word(w):
  return is_triange_number(sum([1 + ord(c) - ord('A') for c in w]))

f = open(path.join(path.dirname(__file__), '../resources/p042_words.txt'))
names = [name.strip('"') for name in f.readline().split(',')]
print(sum([is_triangle_word(name) for name in names]))
