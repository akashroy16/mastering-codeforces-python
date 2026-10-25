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
        idx += 2
        out.append(str((n * m + 1) // 2))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
