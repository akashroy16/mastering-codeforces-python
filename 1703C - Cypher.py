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
        idx += 1 + n
        for i in range(n):
            moves_count = int(data[idx])
            moves = data[idx+1]
            idx += 2
            val = a[i]
            for ch in moves:
                if ch == 'U':
                    val = (val - 1) % 10
                else:
                    val = (val + 1) % 10
            a[i] = val
        out.append(" ".join(map(str, a)))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
