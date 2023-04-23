# Project Euler solutions

The source code for programs used to solve the first 100 Project Euler problems
is found in this repo. Project Euler wishes that its participants do not share
the solutions to problem numbers > 100. I have instead encrypted the source code
using the answer as the passphrase:

```shell
$ python3 euler-0101.py | gpg -d --batch --passphrase-fd 0 euler-101.py.asc
```
