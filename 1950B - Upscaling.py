import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        grid = []
        for r in range(2 * n):
            row = []
            for c in range(2 * n):
                if (r // 2 + c // 2) % 2 == 0:
                    row.append('#')
                else:
                    row.append('.')
            grid.append("".join(row))
        out.append("\n".join(grid))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
