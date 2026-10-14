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
        w = int(data[idx])
        h = int(data[idx+1])
        n = int(data[idx+2])
        idx += 3
        
        sheets = 1
        while w % 2 == 0:
            w //= 2
            sheets *= 2
        while h % 2 == 0:
            h //= 2
            sheets *= 2
            
        if sheets >= n:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
