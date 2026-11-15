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
        x = int(data[idx])
        y = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        req_sticks = k * y + k - 1
        trade1 = (req_sticks + x - 2) // (x - 1)
        total_trades = trade1 + k
        out.append(str(total_trades))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
