import sys
from math import factorial

def solve():
    a, b = map(int, sys.stdin.readline().split())
    print(factorial(min(a, b)))

if __name__ == '__main__':
    solve()
