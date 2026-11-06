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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        counts = Counter(a)
        max_freq = max(counts.values())
        unique_count = len(counts)
        
        ans = max(min(max_freq - 1, unique_count), min(max_freq, unique_count - 1))
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
