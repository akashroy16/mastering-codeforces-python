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
        grid = data[idx:idx+3]
        idx += 3
        for row in grid:
            if '?' in row:
                s = set(row)
                missing = {'A', 'B', 'C'} - s
                out.append(list(missing)[0])
                break
    print("\n".join(out))

if __name__ == '__main__':
    solve()
