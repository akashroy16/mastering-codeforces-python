import sys
import bisect

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    x = [int(v) for v in data[1:n+1]]
    x.sort()
    
    q = int(data[n+1])
    queries = [int(v) for v in data[n+2:n+2+q]]
    
    out = []
    for m in queries:
        ans = bisect.bisect_right(x, m)
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
