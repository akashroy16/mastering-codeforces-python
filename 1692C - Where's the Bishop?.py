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
        grid = data[idx:idx+8]
        idx += 8
        
        found = False
        for r in range(1, 7):
            for c in range(1, 7):
                if grid[r][c] == '#' and grid[r-1][c-1] == '#' and grid[r-1][c+1] == '#' and grid[r+1][c-1] == '#' and grid[r+1][c+1] == '#':
                    out.append(f"{r + 1} {c + 1}")
                    found = True
                    break
            if found:
                break
    print("\n".join(out))

if __name__ == '__main__':
    solve()
