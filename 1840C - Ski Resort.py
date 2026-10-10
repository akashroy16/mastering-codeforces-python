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
        k = int(data[idx+1])
        q = int(data[idx+2])
        a = [int(x) for x in data[idx+3:idx+3+n]]
        idx += 3 + n
        ans = 0
        length = 0
        for temp in a:
            if temp <= q:
                length += 1
            else:
                if length >= k:
                    cnt = length - k + 1
                    ans += cnt * (cnt + 1) // 2
                length = 0
        if length >= k:
            cnt = length - k + 1
            ans += cnt * (cnt + 1) // 2
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
