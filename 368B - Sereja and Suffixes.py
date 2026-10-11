import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    queries = [int(x) for x in data[2+n:2+n+m]]
    
    dp = [0] * n
    seen = set()
    for i in range(n - 1, -1, -1):
        seen.add(a[i])
        dp[i] = len(seen)
        
    out = [str(dp[q - 1]) for q in queries]
    print("\n".join(out))

if __name__ == '__main__':
    solve()
