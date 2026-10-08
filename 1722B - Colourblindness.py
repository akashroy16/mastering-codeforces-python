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
        r1 = data[idx+1]
        r2 = data[idx+2]
        idx += 3
        match = True
        for i in range(n):
            c1 = 'G' if r1[i] == 'B' else r1[i]
            c2 = 'G' if r2[i] == 'B' else r2[i]
            if c1 != c2:
                match = False
                break
        if match:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
