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
        idx += 1
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = a[i]
            nxt = i + a[i]
            if nxt < n:
                dp[i] += dp[nxt]
        out.append(str(max(dp)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
