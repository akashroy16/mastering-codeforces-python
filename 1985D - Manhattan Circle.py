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
        m = int(data[idx+1])
        grid = data[idx+2:idx+2+n]
        idx += 2 + n
        
        rows = []
        cols = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '#':
                    rows.append(r + 1)
                    cols.append(c + 1)
                    
        center_r = (min(rows) + max(rows)) // 2
        center_c = (min(cols) + max(cols)) // 2
        out.append(f"{center_r} {center_c}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
