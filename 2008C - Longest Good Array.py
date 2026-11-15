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
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        diff = r - l
        low, high = 1, 10**9
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            if mid * (mid - 1) // 2 <= diff:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
