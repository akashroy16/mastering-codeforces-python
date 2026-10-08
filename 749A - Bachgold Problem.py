import sys

def solve():
    n = int(sys.stdin.read().strip())
    k = n // 2
    res = [2] * k
    if n % 2 == 1:
        res[-1] = 3
    print(k)
    print(*res)

if __name__ == '__main__':
    solve()
