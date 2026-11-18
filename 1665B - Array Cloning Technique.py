import sys
from collections import Counter

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
        a = data[idx : idx + n]
        idx += n
        mx = max(Counter(a).values())
        ops = 0
        while mx < n:
            ops += 1
            add = min(mx, n - mx)
            ops += add
            mx += add
        out.append(str(ops))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
