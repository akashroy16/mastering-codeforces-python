import sys

def solve():
    n = sys.stdin.readline().strip()
    print(n + n[::-1])

if __name__ == '__main__':
    solve()
