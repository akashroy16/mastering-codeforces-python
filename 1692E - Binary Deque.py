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
        s = int(data[idx + 1])
        idx += 2
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        total_sum = sum(a)
        if total_sum < s:
            out.append("-1")
            continue
        if total_sum == s:
            out.append("0")
            continue
        l = 0
        curr_sum = 0
        max_len = 0
        for r in range(n):
            curr_sum += a[r]
            while curr_sum > s:
                curr_sum -= a[l]
                l += 1
            if curr_sum == s:
                max_len = max(max_len, r - l + 1)
        out.append(str(n - max_len))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
