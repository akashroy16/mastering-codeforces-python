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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        b = [int(x) for x in data[idx+1+n:idx+1+2*n]]
        idx += 1 + 2 * n
        min_a = min(a)
        min_b = min(b)
        moves = 0
        for i in range(n):
            moves += max(a[i] - min_a, b[i] - min_b)
        out.append(str(moves))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
