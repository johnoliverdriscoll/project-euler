from os import path

def is_triange_number(n, t = list()):
  while len(t) == 0 or t[len(t) - 1] < n:
    t.append(((len(t) + 1) * (len(t) + 2)) // 2)
  return n in t

def is_triangle_word(w):
  return is_triange_number(sum(map(lambda c: 1 + ord(c) - ord('A'), w)))

f = open(path.join(path.dirname(__file__), '../resources/p042_words.txt'))
names = list(map(lambda name: name.strip('"'), f.readline().split(',')))
print(sum(map(is_triangle_word, names)))
