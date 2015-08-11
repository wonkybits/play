__author__ = 'philstene'

import sys

numFib = int(raw_input("Please enter the number of Fibonacci numbers to compute.\n"))
fib = []
fib.append(0)
fib.append(1)

for i in range(2, numFib):
    fib.append(fib[i-1] + fib[i-2])

print fib

sys.exit()
