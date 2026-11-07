import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    print(math.factorial(min(a, b)))

if __name__ == '__main__':
    solve()
