import sys

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
        k = int(data[idx+1])
        a = [int(x) for x in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        ans = k
        evens = 0
        for x in a:
            if x % 2 == 0:
                evens += 1
            if x % k == 0:
                ans = 0
            else:
                ans = min(ans, k - (x % k))
                
        if k == 4:
            ans = min(ans, max(0, 2 - evens))
            
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
