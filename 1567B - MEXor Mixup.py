import sys

def xor_to(n):
    rem = n % 4
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n + 1
    return 0

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
        x = xor_to(a - 1)
        if x == b:
            out.append(str(a))
        elif (x ^ b) != a:
            out.append(str(a + 1))
        else:
            out.append(str(a + 2))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
