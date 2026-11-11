import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    presses = [[int(data[i * 3 + j]) for j in range(3)] for i in range(3)]
    grid = [[1]*3 for _ in range(3)]
    dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    for r in range(3):
        for c in range(3):
            k = presses[r][c]
            if k % 2 == 1:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 3 and 0 <= nc < 3:
                        grid[nr][nc] ^= 1
    for r in range(3):
        print("".join(map(str, grid[r])))

if __name__ == '__main__':
    solve()
