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
        a = data[idx]
        b = data[idx+1]
        idx += 2
        
        new_a = b[0] + a[1:]
        new_b = a[0] + b[1:]
        out.append(f"{new_a} {new_b}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
