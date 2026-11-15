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
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        ans = float('inf')
        start = 1 if b == 1 else 0
        for add in range(start, 35):
            cur_b = b + add
            cur_a = a
            ops = add
            while cur_a > 0:
                cur_a //= cur_b
                ops += 1
            if ops < ans:
                ans = ops
        out.append(str(ans))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
