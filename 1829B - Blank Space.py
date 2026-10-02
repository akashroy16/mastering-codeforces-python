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
        
        max_blank = 0
        current = 0
        for val in a:
            if val == 0:
                current += 1
                max_blank = max(max_blank, current)
            else:
                current = 0
                
        out.append(str(max_blank))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
