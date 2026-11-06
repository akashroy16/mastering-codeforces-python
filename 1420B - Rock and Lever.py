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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        counts = defaultdict(int)
        for x in a:
            msb = x.bit_length() - 1
            counts[msb] += 1
            
        ans = 0
        for count in counts.values():
            if count > 1:
                ans += count * (count - 1) // 2
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
