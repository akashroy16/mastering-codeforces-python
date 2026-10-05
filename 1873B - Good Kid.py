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
        
        a.sort()
        a[0] += 1
        
        prod = 1
        for val in a:
            prod *= val
            
        out.append(str(prod))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
