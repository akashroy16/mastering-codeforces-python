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
        m = int(data[idx+1])
        x = data[idx+2]
        s = data[idx+3]
        idx += 4
        
        op = 0
        found = False
        while len(x) <= n * m * 4 or op <= 6:
            if s in x:
                out.append(str(op))
                found = True
                break
            x = x + x
            op += 1
            
        if not found:
            out.append("-1")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
