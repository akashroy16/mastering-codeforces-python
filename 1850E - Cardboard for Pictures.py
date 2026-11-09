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
        c = int(data[idx + 1])
        idx += 2
        s = [int(x) for x in data[idx : idx + n]]
        idx += n
        low, high = 1, 10**9
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for side in s:
                total += (side + 2 * mid) ** 2
                if total > c:
                    break
            if total == c:
                ans = mid
                break
            elif total < c:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
