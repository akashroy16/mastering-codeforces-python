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
        b = int(data[idx + 1])
        idx += 2
        if a > b:
            a, b = b, a
        if b % a != 0:
            out.append("-1")
            continue
        ratio = b // a
        ops = 0
        while ratio % 8 == 0:
            ratio //= 8
            ops += 1
        while ratio % 4 == 0:
            ratio //= 4
            ops += 1
        while ratio % 2 == 0:
            ratio //= 2
            ops += 1
        if ratio == 1:
            out.append(str(ops))
        else:
            out.append("-1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
