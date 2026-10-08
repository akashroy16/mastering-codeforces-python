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
        c = int(data[idx+2])
        idx += 3
        
        ok = False
        if (2 * b - c) > 0 and (2 * b - c) % a == 0:
            ok = True
        if (a + c) % (2 * b) == 0:
            ok = True
        if (2 * b - a) > 0 and (2 * b - a) % c == 0:
            ok = True
            
        if ok:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
