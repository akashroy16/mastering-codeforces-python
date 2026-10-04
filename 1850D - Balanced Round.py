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
        a = [int(x) for x in data[idx+2 : idx+2+n]]
        idx += 2 + n
        
        a.sort()
        max_len = 1
        curr_len = 1
        
        for i in range(1, n):
            if a[i] - a[i-1] <= k:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
            
        out.append(str(n - max_len))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
