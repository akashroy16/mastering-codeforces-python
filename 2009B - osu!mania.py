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
        cols = []
        for _ in range(n):
            row = data[idx]
            idx += 1
            cols.append(row.index('#') + 1)
        out.append(" ".join(map(str, reversed(cols))))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
