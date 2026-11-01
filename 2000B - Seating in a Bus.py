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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        seated = [False] * (n + 2)
        seated[a[0]] = True
        ok = True
        for i in range(1, n):
            pos = a[i]
            if not seated[pos - 1] and not seated[pos + 1]:
                ok = False
                break
            seated[pos] = True
        if ok:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
