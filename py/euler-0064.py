from math import gcd

def is_perfect_square(x):
  x = abs(x)
  return round(x ** (1 / 2)) ** 2 == x

x = 2
odd_periods = 0
while x <= 10000:
  if not is_perfect_square(x):
    i = int(x ** (1 / 2))
    n = i
    d = 1
    digits = 0
    while True:
      i_n = int(d / (x ** (1 / 2) - n))
      d_i_n = d + i_n * n
      h_1 = d_i_n - i_n * n
      h_2 = i_n * x - d_i_n * n
      d = (x - n ** 2) // h_1
      n = h_2 // h_1
      digits += 1
      if n == i and d == 1:
        if digits % 2:
          odd_periods += 1
        break
  x += 1
print(odd_periods)
