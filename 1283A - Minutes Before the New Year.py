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
        h = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        remaining = (23 - h) * 60 + (60 - m)
        out.append(str(remaining))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
