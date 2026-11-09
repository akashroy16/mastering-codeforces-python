import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= k:
                dp[i] = max(dp[i], dp[i - k] + sum(a[i - k : i]))
        out.append(str(dp[n]))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
