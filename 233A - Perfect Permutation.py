import sys

def solve():
    n = int(sys.stdin.read().strip())
    if n % 2 != 0:
        print("-1")
    else:
        res = []
        for i in range(1, n + 1, 2):
            res.append(i + 1)
            res.append(i)
        print(*res)

if __name__ == '__main__':
    solve()
