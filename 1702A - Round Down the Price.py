import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        m = int(data[i])
        power = 1
        while power * 10 <= m:
            power *= 10
        out.append(str(m - power))
    print("\n".join(out))

if __name__ == '__main__':
    solve()
