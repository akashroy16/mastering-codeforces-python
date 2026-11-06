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
        c = int(data[idx+1])
        s = [int(x) for x in data[idx+2:idx+2+n]]
        idx += 2 + n
        
        low = 1
        high = 10**9
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            total_area = sum((x + 2 * mid) ** 2 for x in s)
            if total_area == c:
                ans = mid
                break
            elif total_area < c:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
