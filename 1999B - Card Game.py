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
        a1, a2, b1, b2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        ans = 0
        def check(x1, x2, y1, y2):
            w1 = 1 if x1 > y1 else (0 if x1 == y1 else -1)
            w2 = 1 if x2 > y2 else (0 if x2 == y2 else -1)
            return (w1 + w2) > 0
        if check(a1, a2, b1, b2): ans += 1
        if check(a1, a2, b2, b1): ans += 1
        if check(a2, a1, b1, b2): ans += 1
        if check(a2, a1, b2, b1): ans += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
