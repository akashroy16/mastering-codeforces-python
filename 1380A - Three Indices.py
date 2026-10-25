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
        p = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        found = False
        for i in range(1, n - 1):
            if p[i] > p[i-1] and p[i] > p[i+1]:
                out.append("YES")
                out.append(f"{i} {i+1} {i+2}")
                found = True
                break
        if not found:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
