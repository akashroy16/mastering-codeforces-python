import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    h1 = [int(x) for x in data[1 : n + 1]]
    h2 = [int(x) for x in data[n + 1 : 2 * n + 1]]
    dp0, dp1, dp2 = 0, 0, 0
    for i in range(n):
        ndp0 = max(dp0, dp1, dp2)
        ndp1 = max(dp0, dp2) + h1[i]
        ndp2 = max(dp0, dp1) + h2[i]
        dp0, dp1, dp2 = ndp0, ndp1, ndp2
    print(max(dp0, dp1, dp2))

if __name__ == '__main__':
    solve()
