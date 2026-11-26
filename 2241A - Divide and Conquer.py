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
        if sum(a) % 2 == 0:
            out.append("0")
            continue
        ans = float('inf')
        for x in a:
            ops = 0
            parity = x % 2
            while x % 2 == parity:
                x //= 2
                ops += 1
            if ops < ans:
                ans = ops
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
