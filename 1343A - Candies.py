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
        k = 2
        val = (1 << k) - 1
        while n % val != 0:
            k += 1
            val = (1 << k) - 1
        out.append(str(n // val))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
