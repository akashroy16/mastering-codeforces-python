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
        total_points = 0
        for r in range(10):
            row = data[idx + r]
            for c in range(10):
                if row[c] == 'X':
                    ring = min(r, c, 9 - r, 9 - c) + 1
                    total_points += ring
        idx += 10
        out.append(str(total_points))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
