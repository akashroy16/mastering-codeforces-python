import sys

def solve():
    n = int(sys.stdin.readline().strip())
    if n % 2 == 1:
        print(0)
    else:
        print(1 << (n // 2))

if __name__ == '__main__':
    solve()
