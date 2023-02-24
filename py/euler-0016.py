import sys
e = int(sys.argv[1])
print(sum(map(lambda c: int(c), str(int(2 ** e)))))
