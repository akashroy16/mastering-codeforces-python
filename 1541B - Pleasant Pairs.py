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
        a = [int(x) for x in data[idx+1:idx+1+n]]
        idx += 1 + n
        
        ans = 0
        for i in range(n):
            val = a[i]
            # j ranges such that (i+1)*(j+1) = a[i]*a[j]
            # Since i+1 + j+1 = product / something, we can loop over multiples of val
            start = (val - (i + 1) % val) % val
            if start == 0:
                start = val
            for s in range(start, 2 * n + 1, val):
                j = s - (i + 1)
                if j > i and j < n:
                    if a[i] * a[j] == (i + 1) * (j + 1):
                        ans += 1
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
