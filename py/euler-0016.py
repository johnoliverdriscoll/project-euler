import sys
e = int(sys.argv[1])
print(sum(map(lambda c: int(c), str(2 ** e))))
