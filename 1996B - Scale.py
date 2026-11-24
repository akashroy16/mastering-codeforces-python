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
        k = int(data[idx + 1])
        idx += 2
        grid = data[idx : idx + n]
        idx += n
        for r in range(0, n, k):
            out.append(grid[r][::k])
    print("\n".join(out))

if __name__ == '__main__':
    solve()
