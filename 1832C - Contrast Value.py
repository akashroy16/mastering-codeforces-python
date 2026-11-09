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
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        b = [a[0]]
        for x in a[1:]:
            if x != b[-1]:
                b.append(x)
        if len(b) <= 1:
            out.append("1")
            continue
        ans = 2
        for i in range(1, len(b) - 1):
            if (b[i] > b[i - 1] and b[i] > b[i + 1]) or (
                b[i] < b[i - 1] and b[i] < b[i + 1]
            ):
                ans += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
