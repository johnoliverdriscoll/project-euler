![Project Euler badge](https://projecteuler.net/profile/johnoliverdriscoll.png)

# Project Euler solutions

The source code for programs used to solve the first 100 Project Euler problems
is found in this repo. Project Euler wishes that its participants do not share
the solutions to problem numbers > 100. I have instead encrypted the source code
for problems > 100 with the answer as the passphrase. Therefore, you must
already know the answer to the problem in order to view the solution, so nothing
is spoiled.

Source code is encrypted via command-line using a command similar to this:
```shell
$ python3 euler-0101.py | gpg --symmetric --batch --passphrase-fd 0 euler-101.py.asc
```

Source code can be decrypted via command-line using a command similar to this:
```shell
$ python3 euler-0101.py | gpg --decrypt --batch --passphrase-fd 0 euler-101.py.asc
```
