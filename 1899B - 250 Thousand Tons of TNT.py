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
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + a[i]
        ans = 0
        for k in range(1, n):
            if n % k == 0:
                mn = float('inf')
                mx = -float('inf')
                for i in range(k, n + 1, k):
                    s = pref[i] - pref[i - k]
                    if s < mn:
                        mn = s
                    if s > mx:
                        mx = s
                if mx - mn > ans:
                    ans = mx - mn
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
