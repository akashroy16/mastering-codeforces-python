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
        x = int(data[idx])
        idx += 1
        if x > 45:
            out.append("-1")
            continue
        digits = []
        for d in range(9, 0, -1):
            if x >= d:
                digits.append(str(d))
                x -= d
        out.append("".join(reversed(digits)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
