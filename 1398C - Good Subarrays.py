import sys
from collections import defaultdict

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
        s = data[idx+1]
        idx += 2
        
        counts = defaultdict(int)
        counts[0] = 1
        pref = 0
        ans = 0
        for i, ch in enumerate(s):
            pref += int(ch) - 1
            ans += counts[pref]
            counts[pref] += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
