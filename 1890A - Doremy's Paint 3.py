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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        counts = Counter(a)
        if len(counts) == 1:
            out.append("YES")
        elif len(counts) == 2:
            freqs = list(counts.values())
            if abs(freqs[0] - freqs[1]) <= 1:
                out.append("YES")
            else:
                out.append("NO")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
