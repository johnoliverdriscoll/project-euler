from sys import argv

x = int(argv[1])

def count_rectangles(m, n):
  return (m * (m + 1) // 2) * (n * (n + 1) // 2)

m = 1
while 1:
  if count_rectangles(m, 1) > x:
    break
  m += 1
area, closest = None, None
for i in range(0, m + 1):
  for j in range(i, m + 1):
    rectangles = count_rectangles(i, j)
    if closest == None or abs(rectangles - x) < closest:
      closest = abs(rectangles - x)
      area = i * j
print(area)
