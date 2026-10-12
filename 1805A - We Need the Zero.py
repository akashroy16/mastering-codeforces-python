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
        xor_sum = 0
        for x in a:
            xor_sum ^= x
        if n % 2 == 1:
            out.append(str(xor_sum))
        else:
            if xor_sum == 0:
                out.append("0")
            else:
                out.append("-1")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
