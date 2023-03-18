from sys import argv

n_map = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  15: 'fifteen',
  18: 'eighteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

def to_english(n):
  if n in n_map:
    return n_map[n]
  if n < 20:
    return n_map[n - 10] + 'teen'
  if n < 100:
    return n_map[(n // 10) * 10] + n_map[n % 10]
  if n < 1000:
    if n % 100 == 0:
      return n_map[n // 100] + 'hundred'
    return n_map[n // 100] + 'hundredand' + to_english(n % 100)
  if n % 1000 == 0:
    return n_map[n // 1000] + 'thousand'
  return n_map[n // 1000] + 'thousand' + to_english(n % 1000)

n = int(argv[1])
s = 0
for i in range(1, n + 1):
  s += len(to_english(i))
print(s)
