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
        m = int(data[idx+1])
        s = data[idx+2]
        idx += 3
        counts = Counter(s)
        ans = 0
        for ch in "ABCDEFG":
            if counts[ch] < m:
                ans += m - counts[ch]
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
