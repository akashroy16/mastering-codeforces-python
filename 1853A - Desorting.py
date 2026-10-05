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
        
        min_diff = float('inf')
        is_sorted = True
        
        for i in range(n - 1):
            if a[i] > a[i+1]:
                is_sorted = False
                break
            min_diff = min(min_diff, a[i+1] - a[i])
            
        if not is_sorted:
            out.append("0")
        else:
            out.append(str(min_diff // 2 + 1))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
