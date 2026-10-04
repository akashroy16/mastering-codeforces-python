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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        freq = defaultdict(int)
        ans = 0
        for i, val in enumerate(a):
            diff = val - i
            ans += freq[diff]
            freq[diff] += 1
            
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
