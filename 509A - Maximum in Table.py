import sys

def solve():
    n = int(sys.stdin.read().strip())
    dp = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n-1][n-1])

if __name__ == '__main__':
    solve()
