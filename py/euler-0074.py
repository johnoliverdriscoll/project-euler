from math import factorial

def digital_factorial(n):
  return sum([factorial(int(d)) for d in str(n)])

def digital_factorial_chain_len(n):
  chain = [n]
  while 1:
    n = digital_factorial(n)
    if n in chain:
      return len(chain)
    chain.append(n)

count = 0
for n in range(2, 1000000):
  if digital_factorial_chain_len(n) == 60:
    count += 1
print(count)
