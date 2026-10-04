import sys
import bisect

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    pref = []
    curr = 0
    for x in a:
        curr += x
        pref.append(curr)
        
    m = int(data[1+n])
    queries = [int(x) for x in data[2+n : 2+n+m]]
    
    out = []
    for q in queries:
        idx = bisect.bisect_left(pref, q)
        out.append(str(idx + 1))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
