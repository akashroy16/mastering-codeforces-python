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
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        out.append(f"{min(x, y)} {max(x, y)}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
