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
        a.sort(reverse=True)
        if a[0] == a[-1]:
            out.append("NO")
        else:
            out.append("YES")
            a[1], a[-1] = a[-1], a[1]
            out.append(" ".join(map(str, a)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
