def champernowne(n):
  while len(champernowne.s) < n:
    champernowne.n += 1
    champernowne.s += str(champernowne.n)
  return int(champernowne.s[n - 1])
champernowne.n = 0
champernowne.s = ''

print(
  champernowne(1) \
  * champernowne(10) \
  * champernowne(100) \
  * champernowne(1000) \
  * champernowne(10000) \
  * champernowne(100000) \
  * champernowne(1000000)
)
