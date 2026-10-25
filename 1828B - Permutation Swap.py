import sys
import math

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
        p = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        ans = 0
        for i in range(n):
            diff = abs(p[i] - (i + 1))
            ans = math.gcd(ans, diff)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
