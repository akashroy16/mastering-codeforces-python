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
        b = int(data[idx+1])
        xk = int(data[idx+2])
        yk = int(data[idx+3])
        xq = int(data[idx+4])
        yq = int(data[idx+5])
        idx += 6
        
        moves = set([
            (a, b), (a, -b), (-a, b), (-a, -b),
            (b, a), (b, -a), (-b, a), (-b, -a)
        ])
        
        king_positions = set((xk + dx, yk + dy) for dx, dy in moves)
        queen_positions = set((xq + dx, yq + dy) for dx, dy in moves)
        
        common = king_positions.intersection(queen_positions)
        out.append(str(len(common)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
