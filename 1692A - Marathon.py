import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        
        cnt = (b > a) + (c > a) + (d > a)
        out.append(str(cnt))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
