import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        s = data[i]
        col, row = s[0], s[1]
        res = []
        for c in "abcdefgh":
            if c != col:
                res.append(f"{c}{row}")
        for r in "12345678":
            if r != row:
                res.append(f"{col}{r}")
        out.append("\n".join(res))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
