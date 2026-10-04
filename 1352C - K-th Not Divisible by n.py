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
        idx += 2
        
        ans = k + (k - 1) // (n - 1)
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
