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
        total = 0
        while n > 0:
            total += n
            n //= 2
        out.append(str(total))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
