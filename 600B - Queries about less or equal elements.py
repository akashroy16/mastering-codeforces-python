import sys
import bisect

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    b = [int(x) for x in data[2+n:2+n+m]]
    
    a.sort()
    ans = [str(bisect.bisect_right(a, x)) for x in b]
    print(" ".join(ans))

if __name__ == '__main__':
    solve()
