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
        x = int(data[idx+2])
        idx += 3
        
        min_sum = k * (k + 1) // 2
        max_sum = k * (2 * n - k + 1) // 2
        
        if min_sum <= x <= max_sum:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
