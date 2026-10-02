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
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        out.append(str(b - a))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
