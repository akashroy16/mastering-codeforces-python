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
        
        common = a[0] if a[0] == a[1] or a[0] == a[2] else a[1]
        
        for i in range(n):
            if a[i] != common:
                out.append(str(i + 1))
                break
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
