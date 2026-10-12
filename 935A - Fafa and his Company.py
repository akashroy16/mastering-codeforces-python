import sys

def solve():
    n = int(sys.stdin.read().strip())
    ans = 0
    for i in range(1, n):
        if n % i == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()
