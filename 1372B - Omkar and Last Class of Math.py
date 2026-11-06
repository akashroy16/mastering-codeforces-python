import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        smallest_divisor = n
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                smallest_divisor = d
                break
        if smallest_divisor == n:
            out.append(f"1 {n - 1}")
        else:
            ans1 = n // smallest_divisor
            ans2 = n - ans1
            out.append(f"{ans1} {ans2}")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
