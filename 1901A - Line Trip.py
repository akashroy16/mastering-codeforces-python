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
        x = int(data[idx+1])
        a = [int(v) for v in data[idx+2 : idx+2+n]]
        idx += 2 + n
        
        max_gap = a[0]
        for i in range(1, n):
            max_gap = max(max_gap, a[i] - a[i-1])
            
        max_gap = max(max_gap, 2 * (x - a[-1]))
        out.append(str(max_gap))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
