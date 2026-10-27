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
        d = int(data[idx+3])
        idx += 4
        
        s1 = min(a, b)
        e1 = max(a, b)
        s2 = min(c, d)
        e2 = max(c, d)
        
        in1 = (s1 < s2 < e1)
        in2 = (s1 < e2 < e1)
        if in1 != in2:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
