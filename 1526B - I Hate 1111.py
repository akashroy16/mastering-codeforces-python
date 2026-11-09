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
        idx += 1
        if x >= 111 * 11:
            out.append("YES")
        else:
            if x % 11 <= x // 111:
                out.append("YES")
            else:
                out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
