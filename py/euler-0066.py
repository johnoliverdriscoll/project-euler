# Definitions are sourced from [Continued Fractions and Pell's Equation][1].
#
# [1]: https://math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf

# Definition 1.1
def a_n(a, n):
  i = int(a ** (1 / 2))
  num = i
  den = 1
  for _ in range(0, n):
    i = int(den / (a ** (1 / 2) - num))
    den_i = den + i * num
    h_1 = den_i - i * num
    h_2 = i * a - den_i * num
    den = (a - num ** 2) // h_1
    num = h_2 // h_1
  return i

# Definitions 1.3
def p_n(a, n, p = dict()):
  if n == -1:
    return 1
  if (a, n) not in p:
    if n == 0:
      p[(a, n)] = a_n(a, 0)
    else:
      p[(a, n)] = a_n(a, n) * p_n(a, n - 1) + p_n(a, n - 2)
  return p[(a, n)]

def q_n(a, n, q = dict()):
  if n == -1:
    return 0
  if n == 0:
    return 1
  if (a, n) not in q:
    q[(a, n)] = a_n(a, n) * q_n(a, n - 1) + q_n(a, n - 2)
  return q[(a, n)]

# Definition 1.9
def l_a(a):
  i = int(a ** (1 / 2))
  num = i
  den = 1
  l = 0
  while 1:
    i_num = int(den / (a ** (1 / 2) - num))
    den_i = den + i_num * num
    h_1 = den_i - i_num * num
    h_2 = i_num * a - den_i * num
    den = (a - num ** 2) // h_1
    num = h_2 // h_1
    l += 1
    if num == i and den == 1:
      return l

# Definition 2.5
def solve_pell(d):
  l = l_a(d)
  if l % 2 == 0:
    return (p_n(d, l - 1), q_n(d, l - 1))
  else:
    return (p_n(d, 2 * l - 1), q_n(d, 2 * l - 1))

def is_perfect_square(x):
  x = abs(x)
  return round(x ** (1 / 2)) ** 2 == x

mx, mD = 0, None
for D in [D for D in range(2, 1001) if not is_perfect_square(D)]:
  (x, _) = solve_pell(D)
  if mx < x:
    mx, mD = x, D
print(mD)
