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
        idx += 2
        total = a + 2 * b
        if total % 2 != 0:
            out.append("NO")
        else:
            target = total // 2
            if (target % 2 == 0) or (target % 2 == 1 and a > 0):
                out.append("YES")
            else:
                out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
