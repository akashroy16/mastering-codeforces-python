import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    target = "vika"
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        grid = data[idx : idx + n]
        idx += n
        pos = 0
        for c in range(m):
            if pos < 4 and any(grid[r][c] == target[pos] for r in range(n)):
                pos += 1
        out.append("YES" if pos == 4 else "NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
