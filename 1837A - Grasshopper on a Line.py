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
        k = int(data[idx+1])
        idx += 2
        
        if x % k != 0:
            out.append("1")
            out.append(str(x))
        else:
            out.append("2")
            out.append(f"{x - 1} 1")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
