import sys

def solve():
    n = int(sys.stdin.readline().strip())
    ans = n
    for i in range(1, n):
        ans += (n - i) * i
    print(ans)

if __name__ == '__main__':
    solve()
