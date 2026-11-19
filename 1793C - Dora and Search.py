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
        l, r = 0, n - 1
        mn, mx = 1, n
        while l <= r:
            if a[l] == mn:
                l += 1
                mn += 1
            elif a[l] == mx:
                l += 1
                mx -= 1
            elif a[r] == mn:
                r -= 1
                mn += 1
            elif a[r] == mx:
                r -= 1
                mx -= 1
            else:
                break
        if l <= r:
            out.append(f"{l + 1} {r + 1}")
        else:
            out.append("-1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
