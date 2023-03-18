from sys import argv

e = int(argv[1])
print(sum([int(c) for c in str(2 ** e)]))
