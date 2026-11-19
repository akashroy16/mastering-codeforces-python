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
        if n == 1:
            out.append("2")
        else:
            out.append(str((n + 2) // 3))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
