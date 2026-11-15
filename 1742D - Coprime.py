import sys
from math import gcd

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
        max_idx = {}
        for i, x in enumerate(a):
            max_idx[x] = i + 1
        ans = -1
        vals = list(max_idx.keys())
        for v1 in vals:
            for v2 in vals:
                if gcd(v1, v2) == 1:
                    ans = max(ans, max_idx[v1] + max_idx[v2])
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
