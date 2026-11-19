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
        grid = data[idx : idx + n]
        idx += n
        counts = [row.count('1') for row in grid if '1' in row]
        if len(set(counts)) == 1:
            out.append("SQUARE")
        else:
            out.append("TRIANGLE")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
