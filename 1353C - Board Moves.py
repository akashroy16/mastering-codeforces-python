import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        ans = 0
        k = n // 2
        ans = 8 * k * (k + 1) * (2 * k + 1) // 6
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
