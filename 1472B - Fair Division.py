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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        c1 = a.count(1)
        c2 = a.count(2)
        total = c1 + 2 * c2
        
        if total % 2 != 0:
            out.append("NO")
        else:
            half = total // 2
            # Check if we can achieve 'half' sum using available 2s and 1s
            if half % 2 == 0 or (half % 2 == 1 and c1 > 0):
                out.append("YES")
            else:
                out.append("NO")
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
