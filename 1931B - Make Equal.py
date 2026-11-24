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
        idx += 1
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        target = sum(a) // n
        excess = 0
        ok = True
        for x in a:
            excess += x - target
            if excess < 0:
                ok = False
                break
        out.append("YES" if ok else "NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
